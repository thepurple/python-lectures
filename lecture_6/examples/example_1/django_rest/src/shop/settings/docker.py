"""
Django settings for shop project.

Overwrite some settings for using in docker
"""
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-rest',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'test_postgresql',
        'PORT': '5432',
    },
}
