"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from rest_framework.documentation import include_docs_urls

# va1 libs
from lib.routers import DefaultRouterExt

# API routes
from goods import urls as goods_urls


###############################################################################
# Register API routes
# pylint: disable=invalid-name
router = DefaultRouterExt()
router.extend(goods_urls.router)

# Change admin title
admin.site.site_header = _("Shop administration")
admin.site.site_title = _("Shop site admin")

# URLs without localization
urlpatterns = [
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router.urls), name="api-root"),
    path('api/v1/docs/',
         include_docs_urls(title='Shop API Documentation'),
         name="api-doc"),
    path('admin/', admin.site.urls, name="admin"),
]

urlpatterns += [
    # add and show some landing page
]
