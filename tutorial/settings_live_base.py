from tutorial.settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'tutorial_live',
        'USER': 'tutorial_live',
        'PASSWORD': 'tutorial_live',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = '%s/../media-live/' % BUILDOUT_PATH

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'tutorial_live',
    }
}

CKEDITOR_UPLOAD_PATH = '%s/../media-live/uploads/' % BUILDOUT_PATH

COMPRESS_ENABLED = True
