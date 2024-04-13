"""
Django settings for panopticum project.

Generated by 'django-admin startproject' using Django 2.1.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
import django
from django.utils.translation import gettext
django.utils.translation.ugettext = gettext


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pq9o2n(8u4j57yium2v9xoqnzqnri9j2#+_wy3*%eo^bvowq1w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'corsheaders',
    'database_files',
    'admin_reorder',
    'simple_history',
    'loginas',
    'django_atlassian',
    'panopticum',
    'ckeditor'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'panopticum.pagination.CustomPagination',
    'PAGE_SIZE': 100,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'simple_history.middleware.HistoryRequestMiddleware'
]

ROOT_URLCONF = 'panopticum_django.urls'

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
                'panopticum.context_processors.page_content'
            ],
        },
    },
]

WSGI_APPLICATION = 'panopticum_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('APP_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DB_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', None),
        'PORT': os.environ.get('DB_PORT', None),
        'CONN_MAX_AGE': os.environ.get('DB_CONN_MAX_AGE', 0),
    },
}

if 'JIRA_URL' in os.environ:
    jira_url = os.environ.get('JIRA_URL')
    verify_ssl_env_var = bool(int(os.environ.get('VERIFY_SSL', True)))
    ca_bundle = os.environ.get('CA_CERT', '')
    # Use CA bundle to verify internal resources connectivity if VERIFY_SSL is enabled
    # and the CA_CERT variable is present
    verify = ca_bundle if verify_ssl_env_var and ca_bundle else verify_ssl_env_var

    DATABASES['jira'] = {
        'ENGINE': 'django_atlassian.backends.jira',
        'NAME': jira_url,
        'USER': os.environ.get('JIRA_USER'),
        'PASSWORD': os.environ.get('JIRA_PASSWORD'),
        'SECURITY': '',
        'VERIFY': verify,
    }

DATABASE_ROUTERS = ['django_atlassian.router.Router']

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Admin panel view
# https://github.com/mishbahr/django-modeladmin-reorder

ADMIN_REORDER = (
    # Keep original label and models
    'sites',

    {'app': 'auth', 'models': ('panopticum.User', 'auth.Group')},

    {'app': 'panopticum', 'label': 'Components', 'models':
        ('panopticum.ComponentVersionModel', 'panopticum.ComponentModel')
    },

    {'app': 'panopticum', 'label': 'Products', 'models':
        ('panopticum.ProductFamilyModel', 'panopticum.ProductVersionModel')
    },

    {'app': 'panopticum', 'label': 'Deployments', 'models':
        ('panopticum.DeploymentLocationClassModel', 'panopticum.DeploymentEnvironmentModel', 'panopticum.TCPPortModel')
    },

    {'app': 'panopticum', 'label': 'Active Directory', 'models':
        ('panopticum.CountryModel', 'panopticum.OrganizationModel', 'panopticum.OrgDepartmentModel',
         'panopticum.PersonRoleModel', 'panopticum.User')
    },
    {'app': 'panopticum', 'label': 'requirements',
     'models': (
         'panopticum.Requirement',
         'panopticum.RequirementSet',
     )},
    {'app': 'panopticum', 'label': 'wheels',
     'models': (
         'panopticum.ProgrammingLanguageModel',
         'panopticum.FrameworkModel',
         'panopticum.RuntimeModel',
         'panopticum.ORMModel',
         'panopticum.LoggerModel',
     )},
    {'app': 'panopticum', 'label': 'techradar',
     'models': (
         'panopticum.TechradarRing',
         'panopticum.TechradarQuadrant',
         'panopticum.TechradarEntry',
     )},
)


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Page content

PAGE_TITLE = "Components Registry"
PAGE_FOOTER = "Copyright © 2024"
PAGE_AUTH_REQUIRED = False  # Set PAGE_AUTH_REQUIRED to 'True' to mandate authentication for all pages; otherwise, keep it 'False'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'database_files.storage.DatabaseStorage'
AUTH_USER_MODEL = 'panopticum.User'


# This will only allow admins to log in as other users, as long as
# those users are not admins themselves:
CAN_LOGIN_AS = lambda request, target_user: request.user.is_superuser and not target_user.is_superuser

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

curr_dir = os.path.abspath(os.path.dirname(__file__))
if os.path.exists(os.path.join(curr_dir, "settings_local.py")):
    sys.path.append(curr_dir)
    from settings_local import *
