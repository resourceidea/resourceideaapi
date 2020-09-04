"""
Permissions for the employee module
"""
from rest_framework import permissions


class EmployeePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('employee.add_employee'):
            return True

        if request.user.has_perm('employee.change_employee'):
            return True

        return False


class RecordOwnerOrAdministrator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        can_view_employee = request.user.has_perm('employee.view_employee')
        can_change_employee = request.user.has_perm('employee.change_employee')
        if obj.user == request.user or (can_view_employee and can_change_employee):
            return True

        return False
