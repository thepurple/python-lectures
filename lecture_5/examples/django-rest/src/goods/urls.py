"""
Goods urls for module Patients
"""
from rest_framework import routers
from . import views

# pylint: disable=invalid-name
router = routers.DefaultRouter()
# /api/v1/goods*
router.register('goods', views.GoodsViewSet)

urlpatterns = router.urls
