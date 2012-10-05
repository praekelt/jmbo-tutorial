from tutorial.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'tutorial_qa',
        'USER': 'tutorial_qa',
        'PASSWORD': 'tutorial_qa',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = '%s/../media-qa/' % BUILDOUT_PATH

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'tutorial_qa',
    }
}

CKEDITOR_UPLOAD_PATH = '%s/../media-qa/uploads/' % BUILDOUT_PATH
