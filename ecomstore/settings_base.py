# Base Django settings shared by all environments.
import os

from ecomstore.settings_env import CURRENT_PATH

ADMINS = [
    ('Wangming Ye', 'wangming.ye@gmail.com'),
    ('Store Error Alerts', 'sales@eco-sensa.com'),
]

MANAGERS = ADMINS

UPCOMING_DEAL_ANNOUNCEMENT = '-'
#UPCOMING_DEAL_ANNOUNCEMENT = ''

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

CACHE_TIMEOUT = 60 * 60
PRODUCTS_PER_PAGE = 20
PRODUCTS_PER_ROW = 3
NUM_OF_NEW_ARRIVALS = 25
MINIMUM_FOR_FREE = 25

LOGIN_REDIRECT_URL = '/accounts/my_account/'
SESSION_COOKIE_DAYS = 90
SESSION_COOKIE_AGE = 60 * 60 * 24 * SESSION_COOKIE_DAYS
USE_I18N = False

# Legacy storefront pathing: keep media under /static/ for compatibility.
MEDIA_ROOT = os.path.join(CURRENT_PATH, 'static/')
MEDIA_URL = '/static/'

# Legacy Django/static admin assets path.
ADMIN_MEDIA_PREFIX = '/admin_files/'
STATIC_URL = '/admin_files/'
STATIC_ROOT = os.path.join(CURRENT_PATH, 'admin_files/')
STATICFILES_DIRS = []

SECRET_KEY = 'cvbghwehksqwertyu10'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CURRENT_PATH, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'ecomstore.utils.context_processors.ecomstore',
                'django.template.context_processors.request',
                'ecomstore.django_mobile.context_processors.flavour',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

MIDDLEWARE = (
    'ecomstore.middleware.ExceptionEmailMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'ecomstore.django_ssl.SSLMiddleware.SSLRedirect',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'ecomstore.django_mobile.middleware.MobileDetectionMiddleware',
    'ecomstore.django_mobile.middleware.SetFlavourMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'ecomstore.middleware.FingerprintBlockerMiddleware',
    'ecomstore.middleware.PatternBlockerMiddleware',
    'ecomstore.middleware.RobustIPMiddleware',
    'ecomstore.middleware.AttackMonitorMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

AUTH_PROFILE_MODULE = 'accounts.userprofile'
ROOT_URLCONF = 'ecomstore.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'ecomstore.accounts',
    'ecomstore.catalog',
    'ecomstore.cart',
    'ecomstore.search',
    'ecomstore.checkout',
    'ecomstore.utils',
    'ecomstore.stats',
    'ecomstore.ebay',
    'ecomstore.home',
    'ecomstore.wholesale',
    'ecomstore.misc',
    'ecomstore.dealers',
    'ecomstore.heartwoodbeyond',
    'tagging',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'ecomstore.billing',
    'ecomstore.caching',
    'ecomstore.paypal_driver',
    'ecomstore.RMA',
    'ecomstore.purchases',
    'ecomstore.inventorymanagement',
    'indexer',
    'pagination',
    'sorl.thumbnail',
    'ecomstore.store',
    'trml2pdf',
    'csvimport',
    'ecomstore.newsletter',
    'django.contrib.humanize',
    'ecomstore.nameyourprice',
    'django_model_changes',
    'ecomstore.facebookapp',
    'ecomstore.functionaltests',
    'ecomstore.csvimport_app',
    'django.contrib.staticfiles',
    'ajax_select',
    'import_export',
    'ckeditor',
    'ecomstore.mobile',
    'ecomstore.marketplaces',
    'markdown_deux',
    'bootstrapform',
    'robots',
    'ecomstore.accounting',
    'ecomstore.marketing',
    'ecomstore.referenceusa',
    'social_django',
    'django_object_actions',
    'django_extensions',
    'anymail',
)

CANON_URL_HOST = 'www.your-domain.com'
CANON_URLS_TO_REWRITE = ['your-domain.com', 'other-domain.com']
ANALYTICS_TRACKING_ID = 'UA-37084333-1'
SENTRY_TESTING = True
DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000
