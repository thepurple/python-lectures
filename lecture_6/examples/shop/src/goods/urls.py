"""
Goods's module urls
"""
from django.urls import path

from . import views

# pylint: disable=invalid-name
app_name = 'goods'

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]
