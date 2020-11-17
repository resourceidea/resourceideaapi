"""resourceideaapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # type: ignore
from django.urls import include
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


BASE_API_URL = 'api/v0.1/'

urlpatterns = [
    path('admin/', admin.site.urls),

    path(f'{BASE_API_URL}', include('organization.api.urls')),
    path(f'{BASE_API_URL}', include('employee.api.urls')),
    path(f'{BASE_API_URL}', include('client_industry.api.urls')),
    path(f'{BASE_API_URL}', include('client.api.urls')),
    path(f'{BASE_API_URL}', include('lineofservice.api.urls')),
    path(f'{BASE_API_URL}', include('engagement.api.urls')),
    path(f'{BASE_API_URL}', include('task_assignment.api.urls')),
    path(f'{BASE_API_URL}', include('common.urls')),
    path(f'{BASE_API_URL}', include('department.api.urls')),
    path(f'{BASE_API_URL}', include('job_position.api.urls')),

    path('', include('home.urls')),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
