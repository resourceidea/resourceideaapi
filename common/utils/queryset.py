from typing import Generic
from typing import TypeVar
from uuid import UUID

from django.db.models import QuerySet

from task_assignment.models import TaskAssignment
from organization.models import Organization
from job_position.models import JobPosition
from client.models import Client
from client_industry.models import ClientIndustry
from employee.models import Employee
from engagement.models import Engagement
from department.models import Department
from lineofservice.models import LineOfService

T = TypeVar('T',
            Client,
            ClientIndustry,
            Department,
            Employee,
            Engagement,
            JobPosition,
            LineOfService,
            Organization,
            TaskAssignment)


def filter_by_organization(model: Generic[T], organization_id: UUID) -> QuerySet:  # type: ignore
    """
    Filters active resources that belong to an organization.

    Args:
        model (Generic[T]): Model that is going to be queried.
        organization_id (str): ID of the organization whose clients are to filtered.

    Returns:
        QuerySet of the active resources of an organization whose ID has been supplied.
    """
    queryset = model.objects.filter(organization_id=organization_id, is_deleted=False, deleted_at__isnull=True)  # type: ignore
    return queryset
