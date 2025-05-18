from django.urls import path
from .views import CabinList, CabinDetail, CabinCreate, CabinUpdate, CabinDelete
from django.views.generic import TemplateView


urlpatterns = [
    path('', CabinList.as_view(), name='cabin-list'),
    path('<int:pk>/', CabinDetail.as_view(), name='cabin-detail'),
    path('create/', CabinCreate.as_view(), name='cabin-create'),
    path('update/<int:pk>/', CabinUpdate.as_view(), name='cabin-update'),
    path('delete/<int:pk>/', CabinDelete.as_view(), name='cabin-delete'),
]