import pytest
from rest_framework.reverse import reverse


class TestOrganizationEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_add_organization(self, api_client):
        url = reverse('organization-list')
        response = api_client.post(url, {'name': 'Organization xxx', 'status': 'ACTIVE'})

        response_json = response.json()

        assert response.status_code == 201
        assert 'name' in response_json
        assert 'id' in response_json
        assert response_json['name'] == 'Organization xxx'

    def test_retrieve_organization(self, api_client, organization):
        url = reverse('organization-detail', args=[organization.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert 'name' in response_json
        assert 'status' in response_json
        assert 'id' in response_json

    def test_list_organizations(self, api_client):
        url = reverse('organization-list')
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert isinstance(response_json, list)

    def test_update_organization(self, api_client, organization):
        url = reverse('organization-detail', args=[organization.id])
        response = api_client.put(url, {'name': 'Organization xx 1', 'status': 'ACTIVE'}, format='json')

        response_json = response.json()

        assert response.status_code == 200
        assert 'name' in response_json
        assert 'id' in response_json
        assert 'status' in response_json

    def test_delete_organization(self, api_client, organization):
        url = reverse('organization-detail', args=[organization.id])
        response = api_client.delete(url)
        assert response.status_code == 204
