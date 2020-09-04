# type: ignore
from rest_framework import serializers

from client.api.serializers import ClientSerializer
from common.enums import ProgressStatus
from common.validators.organization_validators import get_request_organization_id
from common.validators.organization_validators import is_organization_user
from engagement.models import Engagement
from lineofservice.api.serializers import LineOfServiceSerializer
from organization.api.serializers import OrganizationSerializer


class EngagementSerializer(serializers.ModelSerializer):
    """Serializes engagement data"""

    organization_id = serializers.UUIDField()
    organization = OrganizationSerializer(read_only=True)
    line_of_service = LineOfServiceSerializer(read_only=True)
    line_of_service_id = serializers.UUIDField(required=False)
    client_id = serializers.UUIDField(required=False)
    client = ClientSerializer(read_only=True)
    manager = serializers.StringRelatedField(read_only=True)
    manager_id = serializers.UUIDField(required=False)
    partner = serializers.StringRelatedField(read_only=True)
    partner_id = serializers.UUIDField(required=False)

    class Meta:
        model = Engagement
        fields = ['id', 'title', 'description', 'planned_start_date',
                  'actual_start_date', 'planned_end_date', 'actual_end_date',
                  'color', 'manager', 'manager_id', 'partner',
                  'partner_id', 'client', 'client_id', 'line_of_service',
                  'line_of_service_id', 'organization', 'organization_id']

    def create(self, validated_data):
        organization_id = get_request_organization_id(request_data=validated_data)
        user_organization_id = self.context['request'].user.employee.organization_id
        is_organization_user(organization_id, user_organization_id)  # TODO (JGS): Log user validation check

        return Engagement.objects.create(
            title=validated_data['title'],
            description=validated_data.get('description', None),
            planned_start_date=validated_data.get('planned_start_date', None),
            planned_end_date=validated_data.get('planned_end_date', None),
            color=validated_data.get('color', None),
            status=ProgressStatus.NOT_STARTED.value,
            partner_id=validated_data.get('partner_id', None),
            manager_id=validated_data.get('manager_id', None),
            client_id=validated_data.get('client_id', None),
            line_of_service=validated_data.get('line_of_service_id', None),
            organization_id=organization_id)
