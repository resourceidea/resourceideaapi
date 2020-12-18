import pytest
from rest_framework.reverse import reverse


class TestJobPositionEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_add_jobposition(self, api_client, organization, department):
        url = reverse('jobposition-list')
        response = api_client.post(url,
                                   {
                                       'title': 'Job position xxyy',
                                       'hierarchy_order': 0,
                                       'department_id': department.id,
                                       'organization_id': organization.id
                                   },
                                   format='json')

        response_json = response.json()

        assert response.status_code == 201
        assert 'id' in response_json
        assert 'title' in response_json

    def test_retrieve_jobposition(self, api_client, job_position):
        url = reverse('jobposition-detail', args=[job_position.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert 'id' in response_json
        assert 'title' in response_json

    def test_list_lineofservice(self, api_client):
        url = reverse('jobposition-list')
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert isinstance(response_json, list)

    def test_update_lineofservice(self, api_client, organization, job_position, department):
        url = reverse('jobposition-detail', args=[job_position.id])
        response = api_client.put(url,
                                  {'title': 'Job position XXX',
                                   'hierarchy_order': 1,
                                   'department_id': department.id,
                                   'organization_id': organization.id},
                                  format='json')

        response_json = response.json()
        job_position.refresh_from_db()

        assert response.status_code == 200
        assert 'id' in response_json
        assert job_position.title == 'Job position XXX'
        assert job_position.hierarchy_order == 1

    def test_delete_lineofservice(self, api_client, job_position):
        url = reverse('jobposition-detail', args=[job_position.id])

        assert job_position.is_deleted is not True
        assert job_position.deleted_at is None

        response = api_client.delete(url)
        job_position.refresh_from_db()

        assert response.status_code == 204
        assert job_position.is_deleted
        assert job_position.deleted_at is not None
