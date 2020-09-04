import pytest
from rest_framework.reverse import reverse


class TestClientIndustryEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_list_client_industries(self, api_client):
        url = reverse('clientindustries-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_add_client_industry(self, api_client, organization) -> None:
        url = reverse('clientindustries-list')
        test_data = {'name': 'Test client name', 'organization_id': organization.id}
        response = api_client.post(url, test_data, format='json')

        response_json = response.json()

        assert response.status_code == 201
        assert response_json['name_slug'] == 'test-client-name'
        assert response_json['organization']['id'] == str(organization.id)

    def test_update_client_industry(self, api_client, organization, client_industry) -> None:
        url = reverse('clientindustries-detail', args=[client_industry.id])
        test_data = {'name': 'Updated client name', 'organization_id': organization.id}
        response = api_client.put(url, test_data, format='json')

        client_industry.refresh_from_db()
        response_json = response.json()

        assert response.status_code == 200
        assert client_industry.name_slug == 'updated-client-name'
        assert response_json['name_slug'] == client_industry.name_slug

    def test_retrieve_client_industry(self, api_client, client_industry) -> None:
        url = reverse('clientindustries-detail', args=[client_industry.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert response_json['name_slug'] == client_industry.name_slug

    def test_delete_department(self, api_client, client_industry):
        url = reverse('clientindustries-detail', args=[client_industry.id])
        response = api_client.delete(url)
        assert response.status_code == 204
