import re

from rest_framework import serializers

from client_industry.models import ClientIndustry
from common.validators.organization_validators import is_organization_user
from common.validators.organization_validators import get_request_organization_id
from organization.api.serializers import OrganizationSerializer


class ClientIndustrySerializer(serializers.ModelSerializer):
    """Client industry serializer"""

    organization_id = serializers.UUIDField(write_only=True)  # type: ignore
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = ClientIndustry
        fields = ('id', 'name', 'name_slug', 'organization', 'organization_id')

    def create(self, validated_data):
        organization_id = get_request_organization_id(request_data=validated_data)
        user_organization_id = self.context['request'].user.employee.organization_id
        is_organization_user(organization_id, user_organization_id)  # TODO (JGS): Log user validation check

        client_industry_name = validated_data.get('name', None)
        if client_industry_name is None:
            raise serializers.ValidationError('name is required')  # type: ignore

        return ClientIndustry.objects.create(name=client_industry_name, organization_id=organization_id)  # type: ignore

    def update(self, instance, validated_data):
        name_slug = re.sub(r'\W', '-', validated_data['name'].lower())
        client_industry_with_slug: ClientIndustry = ClientIndustry.objects.filter(name_slug=name_slug).first()  # type: ignore
        if client_industry_with_slug is not None and instance.id != client_industry_with_slug.id:
            raise serializers.ValidationError('Client industry with name already exists')  # type: ignore

        instance.name = validated_data['name']
        instance.save()
        return instance
