from common.utils.queryset import filter_by_organization
from rest_framework import mixins
from rest_framework import viewsets  # type: ignore
from task_assignment.models import TaskAssignment
from task_assignment.api.serializers import TaskAssignmentSerializer


class TaskAssignmentViewSet(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """Task assignment view set."""

    queryset = TaskAssignment.objects.none()  # type: ignore
    serializer_class = TaskAssignmentSerializer

    def get_queryset(self):
        queryset = filter_by_organization(model=TaskAssignment,  # type: ignore
                                          organization_id=self.request.user.employee.organization_id)
        return queryset
