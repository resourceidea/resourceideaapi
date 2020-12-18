from django.contrib import admin  # type: ignore

from organization.models import Organization

admin.site.register(Organization)
