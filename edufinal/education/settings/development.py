from .common import *
from decouple import config
from pathlib import Path


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(*um10h0_5atc97#j-6qwif^)fm%pr@llsyohp9jm-kwwwj_b%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'edufinal',
        'USER': 'postgres',
        'PASSWORD': 'Easy@123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
