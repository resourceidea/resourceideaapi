import pytest
from rest_framework.reverse import reverse


class TestDepartmentEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_add_department(self, api_client, organization):
        url = reverse('department-list')
        response = api_client.post(url, {'name': 'Department 1', 'organization': organization.id}, format='json')

        response_json = response.json()

        assert response.status_code == 201
        assert 'name' in response_json
        assert response_json['name'] == 'Department 1'
        assert 'organization' in response_json
        assert response_json['organization'] == str(organization.id)

    def test_retrieve_department(self, api_client, department):
        url = reverse('department-detail', args=[department.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert 'name' in response_json
        assert 'id' in response_json
        assert response_json['id'] == str(department.id)
        assert 'organization' in response_json

    def test_list_department(self, api_client):
        url = reverse('department-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_update_department(self, api_client, organization, department):
        url = reverse('department-detail', args=[department.id])
        response = api_client.put(url, {'name': 'Dept 1', 'organization': organization.id}, format='json')

        response_json = response.json()

        assert response.status_code == 200
        assert 'name' in response_json
        assert 'organization' in response_json
        assert 'id' in response_json

    def test_delete_department(self, api_client, department):
        url = reverse('department-detail', args=[department.id])
        response = api_client.delete(url)
        assert response.status_code == 204
