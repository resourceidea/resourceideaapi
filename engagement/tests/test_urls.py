from client.models import Client
import pytest
from rest_framework.reverse import reverse

from engagement.api.serializers import EngagementSerializer
from engagement.models import Engagement


class TestEngagementEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_list_engagements(self, api_client):
        url = reverse('engagement-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_add_engagement(self, api_client, organization, client: Client) -> None:
        url = reverse('engagement-list')
        test_data = {
            'title': 'Test engagement',
            'description': 'Test engagement',
            'color': '#4530e3',
            'organization_id': organization.id,
            'client_id': client.id
        }

        response = api_client.post(url, test_data, format='json')
        response_json = response.json()

        assert response.status_code == 201
        assert response_json['title'] == test_data['title']

    def test_retrieve_engagement(self, api_client, engagement: Engagement) -> None:
        url = reverse('engagement-detail', args=[engagement.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert response_json['title'] == engagement.title

    def test_update_engagement(self, api_client, engagement: Engagement) -> None:
        url = reverse('engagement-detail', args=[engagement.id])
        test_data = EngagementSerializer(engagement).data
        test_data['title'] = 'Updated title'
        response = api_client.put(url, test_data, format='json')

        response_json = response.json()
        engagement.refresh_from_db()

        assert response.status_code == 200
        assert response_json['title'] == engagement.title

    def test_delete_engagement(self, api_client, engagement: Engagement) -> None:
        url = reverse('engagement-detail', args=[engagement.id])
        response = api_client.delete(url)

        assert response.status_code == 204
