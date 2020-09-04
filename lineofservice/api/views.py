from rest_framework import mixins
from rest_framework import viewsets  # type: ignore
from rest_framework.response import Response

from lineofservice.api.serializers import LineOfServiceSerializer
from lineofservice.models import LineOfService


class LineOfServiceViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):

    serializer_class = LineOfServiceSerializer

    def get_queryset(self):
        return LineOfService.objects.filter(organization=self.request.user.employee.organization)  # type: ignore

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(is_deleted=False,
                                   deleted_at__isnull=True,
                                   organization=self.request.user.employee.organization)
        serializer = LineOfServiceSerializer(queryset, many=True)
        return Response(serializer.data)
