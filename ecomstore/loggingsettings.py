"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'DEBUG',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
"""

import os
from logging.handlers import TimedRotatingFileHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(">>> BASE_DIR is:", BASE_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'daily_file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'flashlight.log'),
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'encoding': 'utf-8',
        },
    },

    'loggers': {
        # Root logger — catches everything, including your own modules
        '': {
            'handlers': ['daily_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },

        'django': {
            'handlers': ['daily_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['daily_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        # (Optional) If you only want to capture your own code,
        # scope to your project/app:
        'ecomstore': {
            'handlers': ['daily_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
