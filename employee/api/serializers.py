# type: ignore
from django.contrib.auth.models import User
from rest_framework import serializers

from common.enums import Status
from employee.models import Employee


class EmployeeCreateSerializer(serializers.Serializer):
    """Employee serializer"""

    organization_id = serializers.UUIDField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    file_number = serializers.CharField()
    phone_number = serializers.CharField(required=False)
    status = serializers.ChoiceField(choices=[(status.value, status.value) for status in Status])
    is_resource = serializers.BooleanField(required=False, default=False)
    job_position_id = serializers.UUIDField()

    def create(self, validated_data):
        employee_user_account = User.objects.create(first_name=validated_data['first_name'],
                                                    last_name=validated_data['last_name'],
                                                    username=validated_data['username'],
                                                    email=validated_data['email'],
                                                    is_active=True,
                                                    is_staff=True)

        new_employee = Employee.objects.create(file_number=validated_data['file_number'],
                                               phone_number=validated_data.get('phone_number', None),
                                               status=validated_data['status'],
                                               organization_id=validated_data['organization_id'],
                                               user=employee_user_account,
                                               is_resource=validated_data['is_resource'],
                                               job_position_id=validated_data['job_position_id'])

        return new_employee


class RetrieveUpdateEmployeeSerializer(serializers.ModelSerializer):
    """Serializer for the Employee List view"""

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    job_position_id = serializers.UUIDField()
    organization_id = serializers.UUIDField()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'job_position_id', 'organization_id', 'phone_number',
                  'is_resource', 'status', 'date_terminated']
        depth = 1

    def update(self, instance: Employee, validated_data):

        user_account: User = User.objects.get(pk=instance.user_id)
        user_account.first_name = validated_data['first_name']
        user_account.last_name = validated_data['last_name']
        user_account.save()

        instance.phone_number = validated_data['phone_number']
        instance.job_position_id = validated_data['job_position_id']
        instance.is_resource = validated_data['is_resource']
        instance.status = validated_data['status']
        instance.save()

        return instance


class TerminateEmployeeSerializer(serializers.ModelSerializer):
    """Serializer for the Employee List view"""

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    job_position_id = serializers.UUIDField()
    organization_id = serializers.UUIDField()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'job_position_id', 'organization_id', 'phone_number', 'is_deleted',
                  'is_resource', 'status', 'date_terminated']
