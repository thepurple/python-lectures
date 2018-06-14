"""
Django settings for shop project.

Overwrite some settings for using in docker
"""
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from .base import *

# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
