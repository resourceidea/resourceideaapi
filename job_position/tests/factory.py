import factory
from faker import Faker
from faker.providers import lorem  # type: ignore
from faker.providers import python  # type: ignore

from organization.tests.factory import OrganizationFactory
from department.tests.factory import DepartmentFactory


faker = Faker()

faker.add_provider(lorem)
faker.add_provider(python)


class JobPositionFactory(factory.django.DjangoModelFactory):
    """Job position factory"""

    class Meta:
        model = 'job_position.JobPosition'

    title = faker.word()
    department = faker.word()
    hierarchy_order = faker.pyint(max_value=10)

    department = factory.SubFactory(DepartmentFactory)
    organization = factory.SubFactory(OrganizationFactory)
