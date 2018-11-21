"""
Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

from django.urls import reverse_lazy
##
# from wiki.conf import settings

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b^fv_)t39h%9p40)fnkfblo##jkr!$0)lkp6bpy!fi*f$4*92!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'nomadlife.pythonanywhere.com',
    'localhost',
]


INSTALLED_APPS = [
    'django.contrib.humanize.apps.HumanizeConfig',
    'django.contrib.auth.apps.AuthConfig',
    'django.contrib.contenttypes.apps.ContentTypesConfig',
    'django.contrib.sessions.apps.SessionsConfig',
    'django.contrib.sites.apps.SitesConfig',
    'django.contrib.messages.apps.MessagesConfig',
    ##
    # 'django.contrib.staticfiles',

    'django.contrib.staticfiles.apps.StaticFilesConfig',
    ##
    # 'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    

    'django.contrib.admin.apps.AdminConfig',
    'django.contrib.admindocs.apps.AdminDocsConfig',
    'sekizai',
    'sorl.thumbnail',
    "django_nyt.apps.DjangoNytConfig",
    # "wiki.apps.WikiConfig",
    "wiki.plugins.macros.apps.MacrosConfig",
    'wiki.plugins.help.apps.HelpConfig',
    'wiki.plugins.links.apps.LinksConfig',
    "wiki.plugins.images.apps.ImagesConfig",
    "wiki.plugins.attachments.apps.AttachmentsConfig",
    # "testproject.plugins.attachments.apps.AttachmentsConfig",
    "wiki.plugins.notifications.apps.NotificationsConfig",
    'wiki.plugins.globalhistory.apps.GlobalHistoryConfig',
    'mptt',
    "testproject.apps.MyWikiConfig",
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'testproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'testproject.wsgi.application'


LOGIN_REDIRECT_URL = reverse_lazy('wiki:get', kwargs={'path': ''})


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db', 'prepopulated.db'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'testproject/statics'),
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# STATIC_FINDERS= STATICFILES_FINDERS

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'


WIKI_ANONYMOUS_WRITE = True
WIKI_ANONYMOUS_CREATE = False

# WIKI_ACCOUNT_HANDLING = False
# ACCOUNT_HANDLING = True
WIKI_SIGNUP_URL = '/_test1'
LOGIN_URL = '/_myaccounts/login/'
LOGOUT_URL = '/'

# WIKI_SIGNUP_URL = '/_myaccounts/sign-up/'
# LOGIN_URL = '/_myaccounts/login/'
# LOGOUT_URL = '/_myaccounts/logout/'
