from rest_framework import mixins
from rest_framework import viewsets  # type: ignore

from client.api.serializers import ClientSerializer
from client.models import Client
from common.utils.queryset import filter_by_organization


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Client view set"""

    queryset = Client.objects.none()  # type: ignore
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = filter_by_organization(model=Client, organization_id=self.request.user.employee.organization_id)  # type: ignore
        return queryset
