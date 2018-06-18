"""
Goods urls for module Patients
"""
from rest_framework import routers
from . import views

# pylint: disable=invalid-name
router = routers.DefaultRouter()
router.register('goods', views.GoodsViewSet)

urlpatterns = router.urls
