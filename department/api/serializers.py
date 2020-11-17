from rest_framework import serializers

from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Department serializer"""

    class Meta:
        model = Department
        exclude = ['created_at', 'updated_at', 'is_deleted', 'deleted_at', ]
