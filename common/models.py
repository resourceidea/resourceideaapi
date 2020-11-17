from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    """Base model"""

    id = models.UUIDField(unique=True,
                          primary_key=True,
                          default=uuid4,
                          editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
