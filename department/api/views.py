from rest_framework import mixins  # type: ignore
from rest_framework import viewsets  # type: ignore
from rest_framework.permissions import IsAuthenticated

from common.pagination.defaultconfiguration import CustomPageNumberPagination
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
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Department.objects.filter(organization=self.request.user.employee.organization,
                                             is_deleted=False,
                                             deleted_at__isnull=True)  # type: ignore
        return queryset
