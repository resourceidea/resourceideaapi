from django.db.models.signals import post_save
from django.contrib.auth.models import User
import factory
from faker import Faker
from faker.providers import profile  # type: ignore
from faker.providers import person  # type: ignore
from faker.providers import phone_number  # type: ignore

from common.utils.string_generator import generate_random_string
from employee.tests.factory import EmployeeFactory


faker = Faker()
faker.add_provider(profile)
faker.add_provider(person)
faker.add_provider(phone_number)


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.profile().get('mail')
    username = factory.Sequence(lambda n: f"user_{n}_{generate_random_string(size=6)}")

    employee = factory.RelatedFactory(EmployeeFactory, factory_related_name='user')
