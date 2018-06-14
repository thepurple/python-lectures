"""
va1 urls for module Patients
"""
import logging
from rest_framework import routers
from . import views
logger = logging.getLogger(__package__)

router = routers.DefaultRouter()
router.register('goods', views.GoodsViewSet)

urlpatterns = router.urls
