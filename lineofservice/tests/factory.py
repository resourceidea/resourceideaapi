import factory
from faker import Faker
from faker.providers import lorem  # type: ignore


faker = Faker()
faker.add_provider(lorem)


class LineOfServiceFactory(factory.django.DjangoModelFactory):
    """Line of service factory"""

    class Meta:
        model = 'lineofservice.LineOfService'

    name = faker.word()[:99]

    organization = factory.SubFactory('organization.tests.factory.OrganizationFactory')
