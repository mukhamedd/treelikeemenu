from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<str:item_name>/', views.menu_detail, name='menu_detail' )
]