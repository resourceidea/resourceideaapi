import re

from django.db import models

from client_industry.models import ClientIndustry
from common.models import BaseModel
from organization.models import Organization


class Client(BaseModel):
    """Client model"""

    name = models.CharField(max_length=256, null=False)
    name_slug = models.CharField(max_length=256, editable=False, null=False, blank=False, unique=True)
    address = models.CharField(max_length=256)
    client_industry = models.ForeignKey(ClientIndustry, null=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    src_client_id = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        db_table = 'client'

    def save(self, *args, **kwargs):
        self.name_slug = re.sub(r'\W', '-', self.name.lower())  # type: ignore
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
