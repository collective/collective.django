# coding=utf-8
SERVER_EMAIL = 'root@example.com'
ADMINS = (
    ('manager', 'test@example.com'),
)
MANAGERS = ADMINS
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

TIME_ZONE = 'Europe/Rome'

LANGUAGE_CODE = 'en'

SECRET_KEY = 'testsecret'

ROOT_URLCONF = 'dummyproject.urls'

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'dummypackage'
)

LANGUAGES = (
    ('en', 'English'),
)

SITE_DOMAIN = 'localhost'
SITE_NAME = 'Test'
