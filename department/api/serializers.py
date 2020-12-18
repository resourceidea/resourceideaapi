from rest_framework import serializers

from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Department serializer"""

    class Meta:
        model = Department
        exclude = ['created_at', 'updated_at', 'is_deleted', 'deleted_at', ]

    def to_internal_value(self, data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        if user:
            data['organization'] = user.employee.organization_id
            return super().to_internal_value(data)
