from faker import Faker
from faker.providers import company  # type: ignore
import factory


faker = Faker()
faker.add_provider(company)


class OrganizationFactory(factory.django.DjangoModelFactory):
    name = faker.company()

    class Meta:
        model = 'organization.Organization'
