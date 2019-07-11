from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('new/', views.new_postcode_list, name='new_postcode_list'),
    path('new2/', views.new_postcode_list, name='new_postcode_list'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
]
