from rest_framework import mixins
from rest_framework import viewsets  # type: ignore
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from department.api.serializers import DepartmentSerializer
from department.models import Department


class DepartmentViewSet(mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Department.objects.filter(organization=self.request.user.employee.organization)  # type: ignore

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(is_deleted=False,
                                   deleted_at__isnull=True,
                                   organization=self.request.user.employee.organization)
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)
