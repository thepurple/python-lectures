"""
Poll's module urls
"""
from django.urls import path

from . import views

# pylint: disable=invalid-name
app_name = 'polls'

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
