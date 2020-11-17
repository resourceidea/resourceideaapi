from django.db import models
from django.utils import timezone

from common.models import BaseModel
from organization.models import Organization


class LineOfService(BaseModel):
    """Line of service model"""

    name = models.CharField(max_length=100, null=True, blank=True)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    src_los_id = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = 'line_of_service'
        verbose_name_plural = 'Lines of Service'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name
