from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from client_industry.api.views import ClientIndustryViewSet

router = DefaultRouter()
router.register('', ClientIndustryViewSet, basename='clientindustries')

urlpatterns = [
    path('clientindustries/', include(router.urls), name='clientindustries'),
]
