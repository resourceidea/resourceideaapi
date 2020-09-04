import re
from typing import Dict

from rest_framework import serializers

from client.models import Client
from client_industry.api.serializers import ClientIndustrySerializer
from common.validators.organization_validators import is_organization_user, get_request_organization_id
from organization.api.serializers import OrganizationSerializer


class ClientSerializer(serializers.ModelSerializer):
    """Client serializer"""

    client_industry_id = serializers.UUIDField()  # type: ignore
    client_industry = ClientIndustrySerializer(read_only=True)
    organization_id = serializers.UUIDField()  # type: ignore
    organization = OrganizationSerializer(read_only=True)
    name_slug = serializers.CharField(read_only=True)  # type: ignore

    class Meta:
        model = Client
        fields = ['id', 'name', 'name_slug', 'address', 'organization', 'organization_id', 'client_industry',
                  'client_industry_id']

    def create(self, validated_data):
        organization_id = get_request_organization_id(request_data=validated_data)
        user_organization_id = self.context['request'].user.employee.organization_id
        is_organization_user(organization_id, user_organization_id)  # TODO (JGS): Log user validation check

        client_name = validated_data.get('name', None)
        if client_name is None:
            raise serializers.ValidationError('name is required')  # type: ignore

        return Client.objects.create(name=validated_data['name'],  # type: ignore
                                     address=validated_data['address'],
                                     client_industry_id=validated_data['client_industry_id'],
                                     organization_id=organization_id)

    def update(self, instance: Client, validated_data: Dict):
        name_slug = re.sub(r'\W', '-', validated_data['name'].lower())
        client_with_slug: Client = Client.objects.filter(name_slug=name_slug).first()  # type: ignore
        if client_with_slug is not None and instance.id != client_with_slug.id:
            raise serializers.ValidationError('Client with name already exists')  # type: ignore

        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.client_industry_id = validated_data['client_industry_id']  # type: ignore
        instance.save()
        return instance
