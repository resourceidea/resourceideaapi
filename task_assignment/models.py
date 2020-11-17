from typing import Optional
from client.models import Client
from django.db import models
from django.utils import timezone

from common.enums import ProgressStatus
from common.models import BaseModel
from employee.models import Employee
from organization.models import Organization
from engagement.models import Engagement


class TaskAssignment(BaseModel):
    """Model that holds information about task assignments."""

    class Meta:
        db_table = 'task_assignment'

    task = models.CharField(max_length=128, null=True, blank=True)
    status = models.CharField(max_length=100, choices=[(status.value, status.value) for status in ProgressStatus])
    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    engagement = models.ForeignKey(Engagement, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def engagement_title(self) -> str:
        title: str = ''
        if self.engagement:
            title = self.engagement.title  # type: ignore

        return title

    @property
    def engagement_manager(self) -> str:
        manager: str = ''
        if self.engagement:
            manager = self.engagement.manager.fullname  # type: ignore

        return manager

    @property
    def engagement_partner(self) -> str:
        partner: str = ''
        if self.engagement:
            partner = self.engagement.partner.fullname  # type: ignore

        return partner

    @property
    def client(self) -> Optional[Client]:
        engagement_client: Optional[Client] = None
        if self.engagement_partner:
            engagement_client = self.engagement.client  # type: ignore

        return engagement_client

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return '%s - %s' % (str(self.employee))
