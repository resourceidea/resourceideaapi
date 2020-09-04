from rest_framework import mixins
from rest_framework import viewsets  # type: ignore

from client_industry.api.serializers import ClientIndustrySerializer
from client_industry.models import ClientIndustry


class ClientIndustryViewSet(mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """Client industry viewsets"""

    queryset = ClientIndustry.objects.none()  # type: ignore
    serializer_class = ClientIndustrySerializer

    def get_queryset(self):
        return ClientIndustry.objects.filter(organization_id=self.request.user.employee.organization_id)  # type: ignore
