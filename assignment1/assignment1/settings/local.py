from .settings import *

ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'userlogin',
        'USER': 'merin',
        'PASSWORD': 'inapp',
        'HOST': 'localhost',
        'PORT': '',
    }
}

