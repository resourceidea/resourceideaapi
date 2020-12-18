from common.utils.string_generator import generate_random_string
from job_position.tests.factory import JobPositionFactory
from django.db.models.signals import post_save
import factory
from faker import Faker

from organization.tests.factory import OrganizationFactory


faker = Faker()


@factory.django.mute_signals(post_save)
class EmployeeFactory(factory.django.DjangoModelFactory):
    """Employee factory"""

    class Meta:
        model = 'employee.Employee'
        django_get_or_create = ('user',)

    file_number = factory.Sequence(lambda n: f"FN_{n}{generate_random_string(size=4)}")
    phone_number = factory.Sequence(lambda n: f"F{n}{faker.msisdn()[:9]}")
    status = 'ACTIVE'
    is_resource = True

    organization = factory.SubFactory(OrganizationFactory)
    user = factory.SubFactory('common.tests.factory.user_factory.UserFactory')
    job_position = factory.SubFactory(JobPositionFactory)
