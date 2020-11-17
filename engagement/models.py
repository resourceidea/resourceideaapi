from django.db import models
from django.utils import timezone

from client.models import Client
from common.enums import ProgressStatus
from common.models import BaseModel
from employee.models import Employee
from lineofservice.models import LineOfService
from organization.models import Organization


class Engagement(BaseModel):
    """Model holds information about the engagement details."""

    class Meta:
        db_table = 'engagement'

    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    planned_start_date = models.DateField(null=True, blank=True)
    actual_start_date = models.DateField(null=True, blank=True)
    planned_end_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=7, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[(status.value, status.value) for status in ProgressStatus])
    manager = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, blank=True)
    partner = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name='partner_engagements',
                                blank=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, related_name='manager_engagements',
                               blank=True)
    line_of_service = models.ForeignKey(LineOfService, null=True, on_delete=models.SET_NULL, blank=True)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)

    src_project_id = models.CharField(max_length=40, null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
