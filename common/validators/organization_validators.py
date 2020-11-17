from typing import Dict

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied


def is_organization_user(organization_id: str, user_organization_id: str) -> bool:
    """
    Check if the user belongs to an organization by checking whether the organization
    ID matches the ID of the user's organization.

    Args:
        organization_id (str): Id of the organization.
        user_organization_id (str): Id of the user's organization.
    """
    if organization_id != user_organization_id:
        raise PermissionDenied('User does not have the permission to perform action')
    return True


def get_request_organization_id(request_data: Dict) -> str:
    """
    Get the organization ID from the request data.

    Args:
        request_data (Dict): Request data as a dictionary.

    Returns:
        str if organization_id is included in request_data.

    Raises:
        rest_framework.serializers.ValidationError if organization ID is not
        included in the request data.
    """
    organization_id = request_data.get('organization_id', None)
    if organization_id is None:
        raise serializers.ValidationError('organization_id is required')  # type: ignore
    return organization_id
