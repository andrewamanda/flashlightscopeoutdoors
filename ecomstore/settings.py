"""Compatibility settings module for the ecomstore project.

This keeps DJANGO_SETTINGS_MODULE=ecomstore.settings working while the actual
configuration is split into smaller modules.
"""

from ecomstore.settings_env import BASE_DIR, CURRENT_PATH, PRODUCTION, PRODUCTION_SERVERS
from ecomstore.settings_base import *

if PRODUCTION:
    from ecomstore.settings_production import *
else:
    from ecomstore.settings_local import *

from ecomstore.localsettings import *
from ecomstore.paymentsettings import *
from ecomstore.loggingsettings import *
from ecomstore.celerysettings import *

if not PRODUCTION:
   from ecomstore.mailgunsettings import *

import django
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str
