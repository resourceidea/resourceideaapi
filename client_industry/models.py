import re

from django.db import models
from django.utils import timezone

from common.models import BaseModel
from organization.models import Organization


class ClientIndustry(BaseModel):
    """Client industry model"""

    name = models.CharField(max_length=100, null=False)
    name_slug = models.CharField(max_length=150, editable=False, null=False)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'client_industry'
        verbose_name_plural = 'Client Industries'
        unique_together = ['name', 'name_slug', 'organization']

    def save(self, *args, **kwargs):
        if self.is_deleted is not True:
            self.name_slug = re.sub(r'\W', '-', self.name.lower())  # type: ignore
        super(ClientIndustry, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name
