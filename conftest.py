from typing import List
from employee.models import Employee
from organization.models import Organization

import pytest
from django.core.management import call_command
from faker import Faker
from faker.providers import color  # type: ignore
from faker.providers import company  # type: ignore
from faker.providers import lorem  # type: ignore
from faker.providers import profile  # type: ignore
from pytest_factoryboy import register
from rest_framework.test import APIClient

from client.tests.factory import ClientFactory
from client_industry.tests.factory import ClientIndustryFactory
from common.tests.factory.user_factory import UserFactory
from department.tests.factory import DepartmentFactory
from employee.tests.factory import EmployeeFactory
from engagement.tests.factory import EngagementFactory
from job_position.tests.factory import JobPositionFactory
from lineofservice.tests.factory import LineOfServiceFactory
from organization.tests.factory import OrganizationFactory
from task_assignment.tests.factory import TaskAssignmentFactory

faker = Faker()
faker.add_provider(profile)
faker.add_provider(company)
faker.add_provider(lorem)
faker.add_provider(color)

register(ClientFactory, 'client')
register(OrganizationFactory, 'organization')
register(ClientIndustryFactory, 'client_industry')
register(EmployeeFactory, 'employee')
register(UserFactory, 'user')
register(DepartmentFactory, 'department')
register(JobPositionFactory, 'job_position')
register(EngagementFactory, 'engagement')
register(LineOfServiceFactory, 'line_of_service')
register(TaskAssignmentFactory, 'task_assignment')


@pytest.fixture(scope="function")
def api_client(employee: Employee):
    """Fixture to return the APIClient to be used in the tests."""
    client = APIClient()
    user = employee.user
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def employees_list(organization):
    fake_employees_list: List = []
    for i in range(5):
        fake_employee = EmployeeFactory(organization=organization)  # type: ignore
        if i in [1, 2, 3]:
            fake_employee.is_resource = False
        fake_employee.save()
        fake_employees_list.append(fake_employee)

    return fake_employees_list


@pytest.fixture(scope="session")
def django_setup_db(djang_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "data_dump.json")
