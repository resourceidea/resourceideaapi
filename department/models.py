"""Department app model"""
from django.db import models
from django.utils import timezone

from common.models import BaseModel
from organization.models import Organization


class Department(BaseModel):
    """
    Department model class.

    Holds department information.
    """
    name = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)

    class Meta:
        db_table = 'department'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name
