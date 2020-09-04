import pytest
from rest_framework.reverse import reverse


class TestLineOfServiceEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_add_lineofservice(self, api_client, organization):
        url = reverse('linesofservice-list')
        response = api_client.post(url, {'name': 'LoS xxyy', 'organization_id': organization.id}, format='json')

        response_json = response.json()

        assert response.status_code == 201
        assert 'id' in response_json
        assert 'name' in response_json

    def test_retrieve_lineofservice(self, api_client, line_of_service):
        url = reverse('linesofservice-detail', args=[line_of_service.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert 'id' in response_json
        assert 'name' in response_json

    def test_list_lineofservice(self, api_client):
        url = reverse('linesofservice-list')
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert isinstance(response_json, list)

    def test_update_lineofservice(self, api_client, organization, line_of_service):
        url = reverse('linesofservice-detail', args=[line_of_service.id])
        response = api_client.put(url, {'name': 'Los XXX', 'organization_id': organization.id}, format='json')

        response_json = response.json()

        assert response.status_code == 200
        assert 'id' in response_json
        assert 'name' in response_json

    def test_delete_lineofservice(self, api_client, line_of_service):
        url = reverse('linesofservice-detail', args=[line_of_service.id])
        response = api_client.delete(url)

        assert response.status_code == 204
