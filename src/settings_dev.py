
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
