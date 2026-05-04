from ecomstore.settings_env import PRODUCTION
# Google Checkout API credentials
# sandbox
#GOOGLE_CHECKOUT_MERCHANT_ID = '347567245082398'
#GOOGLE_CHECKOUT_MERCHANT_KEY = 'P91TWTE0sJfjSJ5to4irxg'
#GOOGLE_CHECKOUT_URL = 'https://sandbox.google.com/checkout/api/checkout/v2/merchantCheckout/Merchant/' + #GOOGLE_CHECKOUT_MERCHANT_ID

GOOGLE_CHECKOUT_MERCHANT_ID = '438086541629337'
GOOGLE_CHECKOUT_MERCHANT_KEY = 'YPZs-G-1BSLVxAVuNrslNA'
GOOGLE_CHECKOUT_URL = 'https://checkout.google.com/api/checkout/v2/request/Merchant/' + GOOGLE_CHECKOUT_MERCHANT_ID

# GOOGLE Checkout Production URL:
# https://checkout.google.com/api/checkout/v2/request/Merchant/MERCHANT_ID

# Authorize.Net API Credentials

if not PRODUCTION:
     AUTHNET_POST_URL = 'test.authorize.net'
     AUTHNET_POST_PATH = '/gateway/transact.dll'
     AUTHNET_LOGIN = '3MGL5Tzd7zd'
     AUTHNET_KEY = '9EQ6d39bhT35hcze'
     PAYPAL_USER  = "james_api1.roadtamerus.com"
     PAYPAL_PASSWORD = "BTK6VA44YL6VEGN9"
     PAYPAL_SIGNATURE = "AFcWxV21C7fd0v3bYYYRCpSSRl31A6CpMbLu8yy5jyDs6v.PgvTHVjpu"
     PAYPAL_DEBUG = True

else:
     AUTHNET_POST_URL = 'secure.authorize.net'
     AUTHNET_POST_PATH = '/gateway/transact.dll'
     AUTHNET_LOGIN = '2tSb4TV9Ma5'
     AUTHNET_KEY = '3pnT9Q7r87Kmf5JC'
     PAYPAL_USER = "james_api1.roadtamerus.com"
     PAYPAL_PASSWORD = "N9CCMADGSHG35T94"
     PAYPAL_SIGNATURE = "AYcXGgpx3ifGyKMMNITYnbTK0HTfAgaUDEsdPfr3T7-2tpoJp3ldrWuU"
     PAYPAL_DEBUG = False


STRIPE_WEBHOOK_SECRET = 'whsec_eN01j5wwko9a1HLZOJB0VDUsfN4gCC2X'
