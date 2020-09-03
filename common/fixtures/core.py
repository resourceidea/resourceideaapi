import pytest
from datetime import datetime
from datetime import timedelta

from employee.models import Employee
from organization.models import Organization
from client.models import Client
from common.enums import Status
from common.enums import ProgressStatus
from engagement.models import Engagement
from task_assignment.models import TaskAssignment
from faker import Faker


faker = Faker()


@pytest.fixture
def not_started_task_assignment(django_user_model):
    """Test data for the task assignment table"""
    fake_email = faker.profile()['mail']
    user = django_user_model.objects.create(username=fake_email, email=fake_email, password='strong pass')
    organization = Organization.objects.create(name="Test fake organization", status=Status.ACTIVE.value)  # type: ignore
    client = Client.objects.create(name=faker.company(), organization=organization, address=faker.profile()['address'])  # type: ignore
    employee = Employee.objects.create(user=user, organization=organization, is_resource=True)  # type: ignore
    engagement = Engagement.objects.create(organization=organization, client=client,  # type: ignore
                                           status=ProgressStatus.NOT_STARTED.value,
                                           title=faker.sentence(nb_words=3), color=faker.color(luminosity='bright'),
                                           planned_start_date=datetime.now().date(),
                                           planned_end_date=datetime.now() + timedelta(days=30))

    TaskAssignment.objects.create(organization=organization, status=ProgressStatus.NOT_STARTED.value,  # type: ignore
                                  engagement=engagement, employee=employee,
                                  task=faker.sentence(nb_words=3))
