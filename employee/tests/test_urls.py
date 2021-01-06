from typing import List
from employee.models import Employee
import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from employee.api.serializers import RetrieveUpdateEmployeeSerializer


class TestEmployeeEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db, ]

    def test_list_employees(self, api_client):
        url = reverse('employee-list')
        resp = api_client.get(url)

        resp_body = resp.json()

        assert resp.status_code == 200
        assert isinstance(resp_body, list)

    def test_add_employee(self, api_client, organization, job_position):
        url = reverse('employee-create')
        response = api_client.post(url, {'file_number': '51251',
                                         'organization_id': organization.id,
                                         'phone_number': '0782147101',
                                         'status': 'ACTIVE',
                                         'first_name': 'Test',
                                         'last_name': 'User',
                                         'username': 'testuser',
                                         'email': 'tuser@mail.com',
                                         'job_position_id': job_position.id,
                                         'is_resource': False}, format='json')

        response_json = response.json()

        assert response.status_code == 201
        assert 'first_name' in response_json
        assert response_json['first_name'] == 'Test'
        assert 'last_name' in response_json
        assert response_json['last_name'] == 'User'

        user_account = User.objects.filter(username='testuser')[0]
        assert user_account is not None
        assert user_account.get_full_name() == 'Test User'

    def test_retrieve_employee_details(self, api_client, employee):
        url = reverse('employee-detail', args=[employee.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert 'id' in response_json

    def test_update_employee(self, api_client, employee) -> None:
        """
        Test endpoint url that updates an employee detail.
        """
        url = reverse('employee-detail', args=[employee.id])
        employee_data = RetrieveUpdateEmployeeSerializer(employee).data

        assert employee.first_name == employee_data['first_name']

        first_name_before = employee_data['first_name']
        employee_data['first_name'] = 'Changed'

        response = api_client.put(url, employee_data, format='json')

        employee_query = Employee.objects.get(pk=employee.id)  # type: ignore

        assert response.status_code == 200
        assert first_name_before != employee_data['first_name']
        assert employee_query.first_name == employee_data['first_name']

    def test_delete_employee(self, api_client, employee: Employee) -> None:
        """
        Test deleting an employee
        """
        url = reverse('employee-detail', args=[employee.id])

        assert not employee.is_deleted
        assert employee.deleted_at is None

        resp = api_client.delete(url)

        employee.refresh_from_db()

        assert resp.status_code == 204
        assert employee.is_deleted
        assert employee.deleted_at is not None

    def test_terminate_employee(self, api_client, employee: Employee) -> None:
        """
        Test terminating an employee
        """
        url = reverse('employee-terminate', args=[employee.id])

        assert employee.date_terminated is None
        resp = api_client.patch(url)

        employee.refresh_from_db()

        assert resp.status_code == 200
        assert employee.date_terminated is not None
        assert employee.is_deleted

    @pytest.mark.parametrize('employee__is_resource', [False])
    def test_making_an_employee_a_resource(self, api_client, employee: Employee) -> None:
        """Test making an employee a resource"""
        assert not employee.is_resource

        url = reverse('employee-detail', args=[employee.id])

        employee_data = RetrieveUpdateEmployeeSerializer(employee).data
        assert employee.is_resource == employee_data['is_resource']

        employee_data['is_resource'] = True
        response = api_client.put(url, employee_data, format='json')
        employee.refresh_from_db()

        assert response.status_code == 200
        assert employee.is_resource

    @pytest.mark.parametrize('employee__is_resource', [True])
    def test_remove_employee_from_resources(self, api_client, employee: Employee) -> None:
        assert employee.is_resource

        url = reverse('employee-detail', args=[employee.id])

        employee_data = RetrieveUpdateEmployeeSerializer(employee).data
        assert employee.is_resource == employee_data['is_resource']

        employee_data['is_resource'] = False
        response = api_client.put(url, employee_data, format='json')
        employee.refresh_from_db()

        assert response.status_code == 200
        assert not employee.is_resource

    def test_list_resources_only(self, api_client, employees_list: List[Employee]) -> None:
        url = reverse('employee-list')
        response = api_client.get(url, {'view': 'resources'})

        assert response.status_code == 200
        assert response.request['PATH_INFO'] == '/employees/'
        assert response.request['QUERY_STRING'] == 'view=resources'

    def test_resource_timeline(self, api_client) -> None:
        """
        Test list resource timeline
        """
        url = reverse('resources-timeline')
        response = api_client.get(url)
        response_json = response.json()

        assert response.status_code == 200
        assert "data" in response_json
        assert isinstance(response_json["data"], list)
        assert "assignments" in response_json["data"][0]
        assert "fullname" in response_json["data"][0]
        assert "utilization" in response_json["data"][0]
        assert "job_position" in response_json["data"][0]
        assert "link_url" in response_json["data"][0]
