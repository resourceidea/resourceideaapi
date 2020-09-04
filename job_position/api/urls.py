from django.urls import include, path
from rest_framework.routers import DefaultRouter

from job_position.api.views import JobPositionViewSet

router = DefaultRouter()
router.register('', JobPositionViewSet, basename='jobposition')

urlpatterns = [
    path('jobpositions/', include(router.urls), name='jobpositions')
]
