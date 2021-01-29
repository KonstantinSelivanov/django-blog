"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'di(b9s#(w$^_4=ed^27cycdg@(_0t-t9_4q773ustt#(&1)q&m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 3
SITE_NAME = 'Мой блог'

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    # Site map
    # Карта сайта
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'widget_tweaks',
    'unidecode',
    'captcha',
    'taggit',
    'ckeditor',
    'ckeditor_uploader',
    # CMS
    # 'cms.apps.CmsConfig',
    'django.contrib.admin',
    # Applications
    'pages.apps.PagesConfig',
    'feedback.apps.FeedbackConfig',
    'blog.apps.BlogConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': False,
        'OPTIONS': {
            'loaders': [
                'cms.template.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_blog',
        'USER': 'root',
        'PASSWORD': 'my-sql_20_R00T',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
# flake8: noqa E501
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

# TIME_ZONE = 'Asia/Yekaterinburg'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ----------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SMTP settings
# Configuring messages to be sent to the console instead of using
# an SMTP server
# Настройка отправки сообщений в консоль вместо использования SMTP-сервера
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Email settings
# EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'admin@localhost.ru'
# EMAIL_HOST_PASSWORD = 'mypassword'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# DEFAULT_FROM_EMAIL = 'mymail@mail.ru'

# Tag setings. Without register
TAGGIT_CASE_INSENSITIVE = True


# Captcha settings
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_IMAGE_SIZE = (150, 50)
CAPTCHA_FONT_SIZE = (28)
CAPTCHA_BACKGROUND_COLOR = '#cccccc'
CAPTCHA_FOREGROUND_COLOR = '#001100'
CAPTCHA_LENGTH = 6

# CKeditor settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_ALLOW_NONIMAGE_FILES = True

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_CustomToolbarConfig': [
            {'name': 'item1', 'items': ['Format', 'Font', 'FontSize']},
            {'name': 'item2', 'items': ['Bold', 'Italic', 'Underline',
                                        'Strike']},
            {'name': 'item3', 'items': ['JustifyLeft', 'JustifyCenter',
                                        'JustifyRight', 'JustifyBlock']},
            {'name': 'item4', 'items': ['NumberedList', 'BulletedList']},
            '/',
            {'name': 'item5', 'items': ['Link', 'Image', 'Table',
                                        'SpecialChar']},
            {'name': 'item6', 'items': ['Subscript', 'Superscript',
                                        'TextColor', 'BGColor']},
            {'name': 'item7', 'items': ['Templates', 'Preview',
                                        'Maximize', 'CodeSnippet']},
        ],
        'toolbar': 'CustomToolbarConfig',
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'codesnippet', 'autolink', 'preview'
            ]),
    },

    'user': {
        'skin': 'moono-lisa',
        'toolbar_CustomToolbarConfig': [
            {'name': 'item2', 'items': ['Bold', 'Italic', 'Underline',
                                        'Strike']},
            {'name': 'item5', 'items': ['Link', 'Image', 'Table',
                                        'SpecialChar', 'CodeSnippet',
                                        'Smiley']},
            {'name': 'item4', 'items': ['NumberedList', 'BulletedList']},
            {'name': 'item3', 'items': ['JustifyLeft', 'JustifyCenter',
                                        'JustifyRight', 'JustifyBlock']},
        ],
        'toolbar': 'CustomToolbarConfig',
        'tabSpaces': 4,
        'width': 'auto',
        'extraPlugins': ','.join(
            [
                'codesnippet', 'autolink', 'preview'
            ]),
    }
}


# Site settings
SITE_NAME = 'Записки программиста'
SITE_DESCRIPTION_TITLE = 'Записки программиста'
SITE_DESCRIPTION_TEXT = 'Снипеты: Python, Django, SQL, Linux.'
SITE_COPYRIGHT = 'Copyright © IT Notes 2021'
