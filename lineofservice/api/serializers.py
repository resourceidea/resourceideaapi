from rest_framework import serializers

from lineofservice.models import LineOfService
from organization.api.serializers import OrganizationSerializer


class LineOfServiceSerializer(serializers.ModelSerializer):
    """Line of service serializer"""

    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.UUIDField(write_only=True)  # type: ignore

    class Meta:
        model = LineOfService
        fields = ('id', 'name', 'organization', 'organization_id', )
