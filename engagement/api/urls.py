from engagement.api.views import EngagementViewSet
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', EngagementViewSet, basename='engagement')

urlpatterns = [
    path('engagements/', include(router.urls), name='engagements'),
]
