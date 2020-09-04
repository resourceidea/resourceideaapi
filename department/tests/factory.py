import factory
from faker import Faker
from faker.providers import lorem  # type: ignore

from organization.tests.factory import OrganizationFactory


faker = Faker()
faker.add_provider(lorem)


class DepartmentFactory(factory.django.DjangoModelFactory):
    """Department factory"""

    class Meta:
        model = 'department.Department'

    name = faker.word()

    organization = factory.SubFactory(OrganizationFactory)
