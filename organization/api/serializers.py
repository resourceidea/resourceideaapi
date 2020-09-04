from rest_framework import serializers

from organization.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Organization serializer"""

    class Meta:
        model = Organization
        exclude = ('created_at', 'updated_at', 'is_deleted', 'deleted_at', )
