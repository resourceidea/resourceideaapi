# type: ignore
from rest_framework import serializers

from department.api.serializers import DepartmentSerializer
from job_position.models import JobPosition
from organization.api.serializers import OrganizationSerializer


class JobPositionSerializer(serializers.ModelSerializer):
    """Job position serializer"""

    organization = OrganizationSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = JobPosition
        fields = ['id', 'title', 'hierarchy_order', 'organization', 'department', 'department_id']
