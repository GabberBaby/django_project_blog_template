#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
#author: 'gabber'

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
#author: 'gabber'

# Django settings for django_cms_template project.
from os import path
gettext = lambda s: s

PROJECT_PATH = path.abspath(path.join(path.dirname(__file__), '..'))
STATIC_PATH = path.join(PROJECT_PATH, '../static')
TEMPLATE_PATH = path.join(PROJECT_PATH, '../templates')
#DB_PATH = path.join(PROJECT_PATH, '../{{ project_name }}.db') if db is sqlite uncomment

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Oleg Kupreev', 'oleg@kupreev.pro'),
    ('Igor Kupreev', 'igor@kupreev.pro'),
    ('Drew Executor', 'danmakugato@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"
print MEDIA_ROOT

STATIC_ROOT = path.join(PROJECT_PATH, "../static")
STATIC_URL = "/static/"
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '1uxqmdke&amp;b$h33yspb1*qoet-y*mqj-35vqdfr8e0dza-q0zwl'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'zinnia.context_processors.version',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = TEMPLATE_PATH

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian')
]

INSTALLED_APPS = (
    'fluent_dashboard',

    # enable the admin
    'admin_tools',
    'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',

    #cms
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',

    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
    'reversion',
    'tagging',
    'seo',
    'tinymce',

    #blog
    'mptt',
    'zinnia',
    'photologue',
    'cmsplugin_phlog',


)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


CMS_TEMPLATES = (
    ('index.html', 'index'),
)

CMS_MEDIA_URL = '/static/cms/'

CMS_SEO_FIELDS = True
SEO_FOR_MODELS = []

ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

FLUENT_DASHBOARD_APP_ICONS = {}
FLUENT_DASHBOARD_DEFAULT_MODULE = 'ModelList'
