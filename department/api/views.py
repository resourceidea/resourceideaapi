from rest_framework import mixins
from rest_framework import viewsets  # type: ignore
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

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
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Department.objects.filter(organization=self.request.user.employee.organization,
                                             is_deleted=False,
                                             deleted_at__isnull=True)  # type: ignore
        return queryset
