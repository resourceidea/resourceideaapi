import pytest
from rest_framework.reverse import reverse

from client.api.serializers import ClientSerializer
from client.models import Client


class TestClientEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_list_clients(self, api_client):
        url = reverse('client-list')

        response = api_client.get(url)

        assert response.status_code == 200

    def test_add_client(self, api_client, organization, client_industry) -> None:
        url = reverse('client-list')
        test_data = {'name': 'Test client name', 'address': 'Address 1', 'client_industry_id': client_industry.id,
                     'organization_id': organization.id}
        response = api_client.post(url, test_data, format='json')

        response_json = response.json()

        assert response.status_code == 201
        assert response_json['name_slug'] == 'test-client-name'
        assert response_json['organization']['id'] == str(organization.id)

    def test_retrieve_client(self, api_client, client) -> None:
        url = reverse('client-detail', args=[client.id])

        client_query: Client = Client.objects.get(pk=client.id)  # type: ignore
        assert client_query is not None

        response = api_client.get(url)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json['name_slug'] == client.name_slug

    def test_update_client(self, api_client, client: Client) -> None:
        url = reverse('client-detail', args=[client.id])
        test_data = ClientSerializer(client).data
        test_data['name'] = 'Updated name'
        response = api_client.put(url, test_data, format='json')

        response_json = response.json()
        client.refresh_from_db()

        assert response.status_code == 200
        assert response_json['name_slug'] == client.name_slug

    def test_delete_client(self, api_client, client: Client) -> None:
        url = reverse('client-detail', args=[client.id])
        response = api_client.delete(url)

        assert response.status_code == 204
