import os
import re
import socket

PRODUCTION_SERVERS = [
    '*.webfaction.com',
    '*.whatever.com',
    '*.opalstack.com',
]

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = CURRENT_PATH


def _env_flag(name, default=None):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {'1', 'true', 'yes', 'on'}


def _matches_production_hostname(hostname):
    for pattern in PRODUCTION_SERVERS:
        regex = r'(^.' + pattern + r'$)'
        if re.match(regex, hostname):
            return True
    return False


def is_production():
    env_override = _env_flag('ECOMSTORE_PRODUCTION')
    if env_override is not None:
        return env_override
    return _matches_production_hostname(socket.gethostname())


PRODUCTION = is_production()
