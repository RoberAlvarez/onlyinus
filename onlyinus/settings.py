import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

#SECRET_KEY = '5vmq3r!&#4p=a1f2a12-8f3k2k7kmzh&s7r(s%o7n*)7p5smk@!k'
import os
import environ

env = environ.Env()
environ.Env.read_env()  # By default, reads .env at the project root

SECRET_KEY = env("SECRET_KEY", default="secret-default-key")
#DEBUG = env.bool("DEBUG", default=False)

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#DEBUG = True
ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1', 'onlyinus.com',
                 'onlyinunitedstates.com',
                 'www.onlyinunitedstates.com',
                 'onlyinus-03002030b278.herokuapp.com'
                 ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feedback',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onlyinus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'onlyinus.wsgi.application'

import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL', 'postgres://postgres:Roberto3@localhost:5432/onlyinus'))
}


AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
