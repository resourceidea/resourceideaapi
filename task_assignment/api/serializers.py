# type: ignore
from common.enums import ProgressStatus
from rest_framework import serializers

from common.validators.organization_validators import get_request_organization_id
from common.validators.organization_validators import is_organization_user
from task_assignment.models import TaskAssignment


class TaskAssignmentSerializer(serializers.ModelSerializer):
    """Serializer for the TaskAssignment model."""

    employee_id = serializers.UUIDField()
    organization_id = serializers.UUIDField()
    engagement_id = serializers.UUIDField()

    class Meta:
        model = TaskAssignment
        fields = ['id', 'start_date_time', 'end_date_time', 'employee_id', 'organization_id', 'engagement_id',
                  'task', 'status']

    def create(self, validated_data):
        organization_id = get_request_organization_id(request_data=validated_data)
        user_organization_id = self.context['request'].user.employee.organization_id
        is_organization_user(organization_id, user_organization_id)  # TODO (JGS): Log user validation check

        return TaskAssignment.objects.create(
            task=validated_data['task'],
            start_date_time=validated_data.get('start_date_time', None),
            end_date_time=validated_data.get('end_date_time', None),
            status=ProgressStatus.NOT_STARTED.value,
            employee_id=validated_data.get('employee_id', None),
            engagement_id=validated_data.get('engagement_id', None),
            organization_id=organization_id)
