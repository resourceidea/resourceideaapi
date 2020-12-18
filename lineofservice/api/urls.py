from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from lineofservice.api.views import LineOfServiceViewSet

router = DefaultRouter()
router.register('', LineOfServiceViewSet, basename='linesofservice')

urlpatterns = [
    path('linesofservice/', include(router.urls), name='linesofservice'),
]
