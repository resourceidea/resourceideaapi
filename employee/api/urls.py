from django.urls import path

from employee.api.views import EmployeeCreateView, EmployeeListView
from employee.api.views import EmployeeRetrieveUpdateDeleteView
from employee.api.views import EmployeeTerminateView
from employee.api.views import ResourcesTimelineView

urlpatterns = [
    path('employees/add', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<uuid:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-detail'),
    path('employees/terminate/<uuid:pk>/', EmployeeTerminateView.as_view(), name='employee-terminate'),
    path('dashboard/resources/', ResourcesTimelineView.as_view(), name='resources-timeline'),
]
