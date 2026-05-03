# Production-only overrides.
from ecomstore.settings_env import CURRENT_PATH

DEBUG = False
ENABLE_SSL = True
TEMPLATE_DEBUG = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/wangmingye/apps/heartwoodflooring/memcached.sock',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'roadtamerus__11',
        'USER': 'roadtamerus_1',
        'PASSWORD': 'Wei6ming$$',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET foreign_key_checks = 0;',
        },
    }
}

STATIC_ROOT = CURRENT_PATH + '/admin_files/'
STATICFILES_DIRS = []
