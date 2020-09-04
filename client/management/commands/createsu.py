from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects\
                .filter(username=os.environ.get('SU_USER')).exists():
            User.objects.create_superuser(username=os.environ.get('SU_USER'),
                                          email=os.environ.get('SU_EMAIL'),
                                          password=os.environ.get('SU_PASS'))
