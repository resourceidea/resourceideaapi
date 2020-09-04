import factory
from faker import Faker
from faker.providers import lorem  # type: ignore
from faker.providers import date_time  # type: ignore
import pytz  # type: ignore

from employee.tests.factory import EmployeeFactory
from engagement.tests.factory import EngagementFactory
from organization.tests.factory import OrganizationFactory


faker = Faker()
faker.add_provider(lorem)
faker.add_provider(date_time)


class TaskAssignmentFactory(factory.django.DjangoModelFactory):
    """Task assignment factory"""

    class Meta:
        model = 'task_assignment.TaskAssignment'

    task = faker.sentence(nb_words=3)[:126]
    status = 'NOT STARTED'
    start_date_time = faker.date_time_this_year(tzinfo=pytz.utc)
    end_date_time = faker.date_time_this_year(before_now=False, after_now=True, tzinfo=pytz.utc)

    employee = factory.SubFactory(EmployeeFactory)
    organization = factory.SubFactory(OrganizationFactory)
    engagement = factory.SubFactory(EngagementFactory)
