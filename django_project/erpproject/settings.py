"""
Django settings for erpproject project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent   


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG")

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    
    # Local App
    'layout',
    'authentication.apps.AuthenticationConfig',
    'simple_history',
    'inventory.apps.InventoryConfig',
    'appsystem.apps.AppsystemConfig',
    'company.apps.CompanyConfig',
    'helpdesk.apps.HelpdeskConfig',
    'accounting.apps.AccountingConfig',
    'dms.apps.DmsConfig',
    
    # Third Party App
    'crispy_forms',
    'django.contrib.sites',
    'django.contrib.humanize',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'django_htmx',
    'crispy_bootstrap4',
    'slippers',
    'import_export',
    'django_filters',
    'django_crontab',
    'django_celery_results',
    'django_celery_beat',
    
]

CRONJOBS = [
    ('*/1 * * * *', 'inventory.reports.check_product_stock'),  # Run every 30 minutes
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'erpproject.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
           "builtins": ["slippers.templatetags.slippers"],
        },
    },
]

WSGI_APPLICATION = 'erpproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : config('DB_NAME'),
        'USER' : config('DB_USER'),
        'PASSWORD' : config('DB_PASSWORD'),
        'HOST' : config('DB_HOST'),
        'PORT' : config('DB_PORT')
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Accra'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'assets')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'authentication.User'

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Provider specific settings


TIME_ZONE = 'Africa/Accra'

SOCIALACCOUNT_QUERY_EMAIL = True


LOGIN_REDIRECT_URL = 'authentication/login/'    
LOGOUT_REDIRECT_URL = 'authentication/login/'
# # login url
LOGIN_URL = 'authentication/login/'
SITE_ID = 2
# ACCOUNT_SIGNUP_REDIRECT_URL = "account_logout"
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Provider Configurations

endPoint = config('endPoint')
key = config('key')
Sender_Id = config('Sender_id')


#SMTP CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS',default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


#CELERY SETTINGS
broker_url = 'redis://127.0.0.1:6379'
accept_content = ['application/json']
result_serializer = 'json'
task_serializer = 'json'
timezone = 'Africa/Accra'
result_backend ='django-db'
broker_connection_retry_on_startup = True

#CELERY BEAT SETTINGS
beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'



