from common.validators.organization_validators import is_organization_user
import os

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from department.models import Department
from employee.models import Employee
from job_position.models import JobPosition
from organization.models import Organization


class Command(BaseCommand):
    """
    Custom command to setup a super user in the database if one does not exist.
    """
    help = 'Creates super user'

    def handle(self, *args, **options) -> None:
        user: User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            admin_user = user.objects.create_superuser(username='admin',
                                                       email='admin@resourceidea.com',
                                                       password=os.environ.get('SUPERUSER_PASSWORD'),
                                                       first_name='Joseph',
                                                       last_name='Serunjogi')

            organization: Organization = Organization.objects.create(name='Organization 1',  # type: ignore
                                                                     status='ACTIVE')
            department: Department = Department.objects.create(name='Department 1',  # type: ignore
                                                               organization=organization)
            job_position: JobPosition = JobPosition.objects.create(title='Job Position 1',  # type: ignore
                                                                   hierarchy_order=0,
                                                                   department=department,
                                                                   organization=organization)
            Employee.objects.create(file_number='51251',  # type: ignore
                                    phone_number='0711187734',
                                    phone_number_confirmed=True,
                                    status='ACTIVE',
                                    user=admin_user,
                                    organization=organization,
                                    is_resource=True,
                                    email_confirmed=True,
                                    job_position=job_position)
