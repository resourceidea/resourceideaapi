from django.urls import path

from common.views import index
from common.views import sentry_debug


urlpatterns = [
    path('initialsetup/', index, name='initialsetup'),
    path('sentry-debug/', sentry_debug, name='sentry-debug'),
]
