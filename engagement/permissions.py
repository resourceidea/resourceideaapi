"""
Permissions for the engagement model.
"""
from rest_framework import permissions


class EngagementPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create' \
                and request.user.has_perm('engagement.add_engagement'):
            return True

        if view.action in ['update', 'partial_update'] \
                and request.user.has_perm('engagement.change_engagement'):
            return True

        if view.action in ['list', 'retrieve'] \
                and request.user.has_perm('engagement.view_engagement'):
            return True

        return False
