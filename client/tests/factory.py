import factory
from faker import Faker
from faker.providers import profile  # type: ignore

from organization.tests.factory import OrganizationFactory
from client_industry.tests.factory import ClientIndustryFactory


faker = Faker()
faker.add_provider(profile)


class ClientFactory(factory.django.DjangoModelFactory):
    """Client factory"""

    class Meta:
        model = 'client.Client'

    name = faker.profile().get('company', 'Test client 1')
    address = faker.profile().get('address', None)

    organization = factory.SubFactory(OrganizationFactory)
    client_industry = factory.SubFactory(ClientIndustryFactory)
