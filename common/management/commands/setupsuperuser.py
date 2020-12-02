import os

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    """
    Custom command to setup a super user in the database if one does not exist.
    """
    help = 'Creates super user'

    def handle(self, *args, **options) -> None:
        user: User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            user.objects.create_superuser(username='admin',
                                          email='admin@resourceidea.com',
                                          password=os.environ.get('SUPERUSER_PASSWORD'))
