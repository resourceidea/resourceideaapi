import factory
from faker import Faker
from faker.providers import date_time  # type: ignore
from faker.providers import lorem  # type: ignore
from faker.providers import color  # type: ignore


faker = Faker()
faker.add_provider(date_time)
faker.add_provider(lorem)
faker.add_provider(color)


class EngagementFactory(factory.django.DjangoModelFactory):
    """Engagement factory"""

    class Meta:
        model = 'engagement.Engagement'

    title = faker.sentence(nb_words=3)
    description = faker.sentence(nb_words=8)
    planned_start_date = faker.date_this_year()
    actual_start_date = faker.date_this_year(before_today=False, after_today=True)
    planned_end_date = faker.date_this_year(before_today=False, after_today=True)
    actual_end_date = faker.date_this_year(before_today=False, after_today=True)
    color = faker.hex_color()
    status = 'NOT STARTED'
    organization = factory.SubFactory('organization.tests.factory.OrganizationFactory')
    line_of_service = factory.SubFactory('lineofservice.tests.factory.LineOfServiceFactory')
    client = factory.SubFactory('client.tests.factory.ClientFactory')
    manager = factory.SubFactory('employee.tests.factory.EmployeeFactory')
    partner = factory.SubFactory('employee.tests.factory.EmployeeFactory')
