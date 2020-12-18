from django.contrib import admin  # type: ignore
from client.models import Client


admin.site.register(Client)
