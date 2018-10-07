from base import *
 
DEBUG = True
 
INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_huXVMABXPzJmtBClroUo7vFA')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_qgkn8rHXvHGEtPaqreOCeXi7')
 
