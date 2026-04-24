#EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
#MAILGUN_ACCESS_KEY = 'key-bf97730316409b49c6500064cb782549'
#MAILGUN_SERVER_NAME = 'andrew-amanda.com'

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "key-bf97730316409b49c6500064cb782549",
    "MAILGUN_SENDER_DOMAIN": 'andrew-amanda.com',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "sales@andrew-amanda.com"  # if you don't already have this in settings
SERVER_EMAIL = "sales@andrew-amanda.com"  # ditto (default from-email for Django errors)
