import os
import logging

import environ


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

env = environ.Env()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'debug_toolbar',

    #Local
    'apps.templates_app',
    'apps.users',
    'apps.taplink',
    'apps.shop',
    'apps.customer',
    'django_cleanup.apps.CleanupConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Third party
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.shop.context_processors.pathname',
                'apps.shop.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

try:
    from .local import *
except ImportError:
    try:
        from .prod import *
    except ImportError:
        logging.error('core.settings.prod.py file not found !')
        exit()


AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'index_page'
LOGOUT_REDIRECT_URL = 'index_page'

INTERNAL_IPS = ['127.0.0.1']

CART_SESSION_ID = 'cart'

PAYBOX_MERCHANT_ID = env.int('PAYBOX_MERCHANT_ID')
PAYBOX_SECRET_KEY = env.str('PAYBOX_SECRET_KEY')

PAYBOX_URL = 'https://api.paybox.money/'
