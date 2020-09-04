from task_assignment.models import TaskAssignment
import pytest
from rest_framework.reverse import reverse

from employee.models import Employee
from engagement.models import Engagement
from organization.models import Organization
from task_assignment.api.serializers import TaskAssignmentSerializer


class TestTaskAssignmentEndpoints:
    pytestmark = [pytest.mark.system, pytest.mark.django_db]

    def test_list_task_assignment(self, api_client) -> None:
        """Test listing task assignments"""
        url = reverse('taskassignment-list')
        response = api_client.get(url)

        assert response.status_code == 200

    def test_add_task_assignment(self,
                                 api_client,
                                 organization: Organization,
                                 engagement: Engagement,
                                 employee: Employee) -> None:
        """Test add task assignment"""
        url = reverse('taskassignment-list')
        test_data = {
            'task': 'Task 1',
            'status': 'NOT STARTED',
            'start_date_time': '2020-08-01T09:00:00',
            'end_date_time': '2020-08-20T17:00:00',
            'organization_id': organization.id,
            'employee_id': employee.id,
            'engagement_id': engagement.id
        }

        response = api_client.post(url, test_data, format='json')
        response_json = response.json()

        assert response.status_code == 201
        assert 'task' in response_json
        assert response_json['task'] == test_data['task']

    def test_retrieve_task_assignment(self, api_client, task_assignment: TaskAssignment) -> None:
        """Test retrieving a task assignment"""
        url = reverse('taskassignment-detail', args=[task_assignment.id])
        response = api_client.get(url)

        response_json = response.json()

        assert response.status_code == 200
        assert response_json['task'] == task_assignment.task

    def test_update_task_assignment(self, api_client, task_assignment: TaskAssignment) -> None:
        """Test updating a task assignment"""
        url = reverse('taskassignment-detail', args=[task_assignment.id])

        test_data = TaskAssignmentSerializer(task_assignment).data
        test_data['task'] = 'Task updated'

        response = api_client.put(url, test_data, format='json')
        response_json = response.json()
        task_assignment.refresh_from_db()

        assert response.status_code == 200
        assert response_json['task'] == task_assignment.task == 'Task updated'

    def test_delete_task_assignment(self, api_client, task_assignment: TaskAssignment) -> None:
        """Test deleting a task assignment"""
        url = reverse('taskassignment-detail', args=[task_assignment.id])
        response = api_client.delete(url)

        assert response.status_code == 204
