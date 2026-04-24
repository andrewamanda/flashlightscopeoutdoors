# Local development overrides.
import os

from ecomstore.settings_env import CURRENT_PATH

DEBUG = True
ENABLE_SSL = False
TEMPLATE_DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flashlights',
        'USER': 'root',
        'PASSWORD': 'Wei6ming',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET foreign_key_checks = 0;',
        },
    }
}

STATIC_ROOT = os.path.join(CURRENT_PATH, '_collected_static')
STATICFILES_DIRS = [
    os.path.join(CURRENT_PATH, 'admin_files'),
    os.path.join(CURRENT_PATH, 'static'),
]

ALLOWED_HOSTS = [
    '127.0.0.1',
    '[::1]',
    'localhost',
    '192.168.86.29',
    '192.168.1.214',
    '192.168.1.57',
]
