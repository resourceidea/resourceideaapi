from common.utils.date_utils import get_working_hours
from datetime import date, datetime, time
from typing import Dict
from typing import List
from uuid import UUID

from django.db.models.query import QuerySet
from rest_framework.reverse import reverse

from common.utils.queryset import filter_by_organization
from employee.models import Employee
from task_assignment.models import TaskAssignment
from task_assignment import utils as task_assignment_utils


def get_resource_utilization(resource_assignments: List[Dict], start_date: date, end_date: date) -> float:
    """Get the utilization of a resource in a given period
    Args:
        resource_assignments (List[Dict]): List of assignments to the resource.
        start_date (date): Start date for the period to get the utilization for.
        end_date (date): End date for the period to get the utilization for.

    Returns:
        Utilization score as a percentage value.
    """
    utilization_score: float = 0.0
    period_start: datetime = datetime.combine(start_date, time(8, 0, 0))
    period_end: datetime = datetime.combine(end_date, time(17, 0, 0))
    total_period_hours: float = get_working_hours(period_start, period_end)

    if resource_assignments:
        total_assignment_hours: float = 0.0
        for assignment in resource_assignments:
            assigned_hours: float = get_working_hours(assignment['start_date'], assignment['end_date'])
            total_assignment_hours += assigned_hours
        utilization_score = (total_assignment_hours / total_period_hours) * 100

    return utilization_score


def get_resource_assignments(resource_id: UUID, organization_id: UUID, start_date: date, end_date: date) -> List[Dict]:
    """Get the assignments made to a resource in a given period

    Args:
        resource_id(UUID): Resource ID.
        start_date(date): Start date for the period that the assignments are being queried.
        end_date(date): End date for the period that the assignments are being queried.

    Returns:
        Assignments made to a resource as a list of dictionaries.
    """
    # TODO (Joseph Serunjogi): Restrict to period to a month. To be updated to other periods.
    resource_assignments: List[Dict] = []
    assignments_queryset: QuerySet = filter_by_organization(model=TaskAssignment, organization_id=organization_id)  # type: ignore
    if assignments_queryset:
        assignments: List[TaskAssignment] = list(assignments_queryset.filter(employee__id=resource_id,
                                                                             start_date_time__gte=start_date,
                                                                             end_date_time__lte=end_date))

        for assignment in assignments:
            entry: Dict = {
                'client': {
                    'name': assignment.client.name,
                    'client_id': assignment.client.id
                },
                'engagement': {
                    'title': assignment.engagement_title,
                    'manager': assignment.engagement_manager,
                    'partner': assignment.engagement_partner,
                    'link_url': task_assignment_utils.get_task_assignment_link_url(assignment.id)
                },
                'start_date': assignment.start_date_time,
                'end_date': assignment.end_date_time
            }

            resource_assignments.append(entry)

    return resource_assignments


def get_resource_link_url(resource_id: UUID) -> str:
    """Get the link to the resource's profile url.

    Args:
        resource_id(UUID): Resource ID.

    Returns:
        Resource's relative url as a string.
    """
    link_url: str = reverse('employee-detail', args=[resource_id])
    return link_url


def get_resource_timelines_by_date(organization_id: UUID, start_date: date, end_date: date) -> List[Dict]:
    """Get the resources assignments timeline in a given period.

    Args:
        organization_id (UUID): ID of the organization whose resources' timelines are to be returned.
        start_date (date): Start date for the timeline period that is being queried.
        end_date (date): End date for the timeline period that is being queried.

    Returns:
        Resources' assignment timelines as a list of dictionaries.
    """
    resource_timeline_list: List[Dict] = []

    resources_queryset: QuerySet = filter_by_organization(model=Employee, organization_id=organization_id)  # type: ignore
    if resources_queryset:
        resources_queryset: QuerySet = resources_queryset.filter(is_resource=True)

        organization_resources: List[Employee] = list(resources_queryset)
        for resource in organization_resources:
            assignments: List[Dict] = get_resource_assignments(resource.id, organization_id, start_date, end_date)
            utilization_score: float = get_resource_utilization(assignments, start_date, end_date)

            resource_timeline: Dict = {
                'fullname': resource.fullname,
                'utilization': utilization_score,
                'job_position': resource.job_position_title,
                'link_url': get_resource_link_url(resource.id),
                'assignments': assignments
            }

            resource_timeline_list.append(resource_timeline)

    return resource_timeline_list
