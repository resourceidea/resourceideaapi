from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from common.enums import Status
from common.models import BaseModel
from job_position.models import JobPosition
from organization.models import Organization


class Employee(BaseModel):
    """Employee model."""

    file_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    phone_number_confirmed = models.BooleanField(null=False, default=False)
    status = models.CharField(max_length=10, choices=[(status.value, status.value) for status in Status])

    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    is_resource = models.BooleanField(null=False, default=False)
    email_confirmed = models.BooleanField(null=False, default=False)
    job_position = models.ForeignKey(JobPosition, null=True, on_delete=models.SET_NULL)
    date_terminated = models.DateField(null=True, blank=True)
    src_resource_id = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        db_table = 'employee'

    @property
    def fullname(self):
        return self.user.get_full_name()  # type: ignore

    @property
    def first_name(self):
        return self.user.first_name  # type: ignore

    @property
    def last_name(self):
        return self.user.last_name  # type: ignore

    @property
    def email(self):
        return self.user.email  # type: ignore

    @property
    def job_position_title(self):
        title = None
        if self.job_position is not None:
            title = self.job_position.title  # type: ignore
        return title

    @property
    def username(self):
        return self.user.username  # type: ignore

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)  # type: ignore
