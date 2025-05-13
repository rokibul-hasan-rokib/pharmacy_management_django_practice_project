from django.urls import path
from .views import UserList, UserDetail, UserCreate, UserUpdate, UserDelete

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/create/', UserCreate.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', UserDelete.as_view(), name='user-delete'),
]