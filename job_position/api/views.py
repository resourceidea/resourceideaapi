from rest_framework import mixins
from rest_framework import viewsets  # type: ignore
from rest_framework.response import Response

from job_position.api.serializers import JobPositionSerializer
from job_position.models import JobPosition


class JobPositionViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = JobPositionSerializer

    def get_queryset(self):
        return JobPosition.objects.filter(organization=self.request.user.employee.organization)  # type: ignore

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(is_deleted=False,
                                   deleted_at__isnull=True,
                                   organization=self.request.user.employee.organization)
        serializer = JobPositionSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        TODO: Customize the job position create operation
        """
        return super().create(request, *args, **kwargs)
