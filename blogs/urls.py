from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<int:pk>/update/', views.blog_update, name='blog_update'),
    path('blog/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]

