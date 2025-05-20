from django.urls import path
from .views import (
    EmployeeList,
    EmployeeDetail,
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeDelete,
)

urlpatterns = [
    path('', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('employee/create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employee/update/<int:pk>/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee/delete/<int:pk>/', EmployeeDelete.as_view(), name='employee-delete'),
]