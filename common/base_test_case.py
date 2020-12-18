from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from common.utils import create_administrator_groups  # type: ignore
from common.utils import create_resource_groups  # type: ignore
from organization.models import Organization


class BaseAPITestCase(APITestCase):
    user_username = 'testuser'
    user_password = 'strongkey'

    def setUp(self):
        create_administrator_groups()
        create_resource_groups()
        self.user = User.objects.create_user(username=self.user_username,
                                             password=self.user_password,
                                             first_name='Serunjogi',
                                             last_name='Joseph')
        self.user.is_active = True
        self.user.save()
        self.organization = Organization.objects.create(name='Test Org',  # type: ignore
                                                        status='active')
        response = self.client.post(
            '/api/token/',
            data={'username': self.user_username,
                  'password': self.user_password})
        self.access_token = response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
