from .base import *

# Sobreescribimos el DEBUG de base.py
DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            #
        }
    }
}