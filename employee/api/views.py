from calendar import monthrange
from datetime import date, datetime
from typing import NewType, Tuple
from uuid import UUID

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework.response import Response
from rest_framework.views import APIView

from common.exceptions import InvalidOperationException
from employee.api.serializers import (EmployeeCreateSerializer,
                                      RetrieveUpdateEmployeeSerializer,
                                      TerminateEmployeeSerializer)
from employee.models import Employee
from employee.utils.resources import get_resource_timelines_by_date

OrganizationId = NewType('OrganizationId', UUID)  # OrganizationId type


def _employee_queryset(organization_id: OrganizationId) -> QuerySet:
    """
    Returns the active employees queryset
    """
    return Employee.objects.filter(organization_id=organization_id,  # type: ignore
                                   is_deleted=False,
                                   deleted_at__isnull=True,
                                   date_terminated__isnull=True)


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.none()  # type: ignore
    serializer_class = EmployeeCreateSerializer

    def get_queryset(self):
        return _employee_queryset(organization_id=self.request.user.employee.organization_id)


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.none()  # type: ignore
    serializer_class = RetrieveUpdateEmployeeSerializer

    def get_queryset(self):
        queryset = _employee_queryset(organization_id=self.request.user.employee.organization_id)
        view = self.request.query_params.get('view', None)
        if view is not None and view == 'resources':
            queryset = queryset.filter(is_resource=True)

        return queryset


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.none()  # type: ignore
    serializer_class = RetrieveUpdateEmployeeSerializer

    def get_queryset(self):
        return _employee_queryset(organization_id=self.request.user.employee.organization_id)


class EmployeeTerminateView(APIView):
    def patch(self, request, pk):
        # TODO (Joseph Serunjogi): Log entry of employee terminate view method.
        employee = get_object_or_404(Employee, pk=pk)

        date_terminated = timezone.now().strftime('%Y-%m-%d')
        data = {"date_terminated": date_terminated, "is_deleted": True}
        serializer = TerminateEmployeeSerializer(employee, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourcesTimelineView(APIView):
    """List the resources timeline dashboard"""
    def _set_default_period_inputs(self) -> Tuple[str, str]:
        month_start, month_end = monthrange(datetime.today().year, datetime.today().month)
        from_input = f"{datetime.today().year}-{datetime.today().month}-{month_start}"
        to_input = f"{datetime.today().year}-{datetime.today().month}-{month_end}"

        return from_input, to_input

    def _convert_string_to_date(self, date_string: str) -> datetime:
        return datetime.strptime(date_string, "%Y-%m-%d")

    def _convert_period_input(self, from_input: str, to_input: str) -> Tuple[datetime, datetime]:

        if from_input is None or to_input is None:
            from_input, to_input = self._set_default_period_inputs()

        try:
            from_conversion: datetime = self._convert_string_to_date(from_input)
            to_conversion: datetime = self._convert_string_to_date(to_input)
        except ValueError:
            from_input, to_input = self._set_default_period_inputs()
            from_conversion: datetime = self._convert_string_to_date(from_input)
            to_conversion: datetime = self._convert_string_to_date(to_input)

        return from_conversion, to_conversion

    def get(self, request, format=None):
        # TODO (Joseph Serunjogi): Log entry of resource timeline view method.
        organization_id: UUID = self.request.user.employee.organization_id
        from_input: str = self.request.query_params.get('from', None)
        to_input: str = self.request.query_params.get('to', None)

        from_conversion, to_conversion = self._convert_period_input(from_input, to_input)
        start_date: date = from_conversion.date()
        end_date: date = to_conversion.date()

        response: dict = {}
        try:
            response['data'] = get_resource_timelines_by_date(organization_id, start_date, end_date)
        except InvalidOperationException as error:
            # TODO (Joseph Serunjogi): Log invalid operation exception.
            response['data'] = error
        # TODO (Joseph Serunjogi): Log exit of resource timeline view method.
        return Response(response)
