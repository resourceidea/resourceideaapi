from uuid import UUID
from rest_framework.reverse import reverse


def get_task_assignment_link_url(task_assignment_id: UUID) -> str:
    link_url: str = reverse('taskassignment-detail', args=[task_assignment_id])
    return link_url
