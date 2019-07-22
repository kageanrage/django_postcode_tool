from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('new/', views.new_postcode_list, name='new_postcode_list'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
    path('list/<int:pk>/edit/', views.list_edit, name='list_edit'),
    path('list/<int:pk>/delete/', views.list_remove, name='list_remove'),
    path('about/', views.about, name='about'),
]
