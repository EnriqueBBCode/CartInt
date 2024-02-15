from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-7ic$1a2*9_^ly=_8(822cb@n++szwa(or#&*r*1b8y=a+d6rz='

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'Main',
    'Contacts',
    'django_recaptcha',
]

RECAPTCHA_PUBLIC_KEY = '6LfnWmApAAAAAGaYFMRi2kRQffhQ7iUNuNq_yIak'
RECAPTCHA_PRIVATE_KEY = '6LfnWmApAAAAAEB8Cp9GJmA11ytA-cmSZNjiRRth'
RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}
RECAPTCHA_DOMAIN = 'expresscuba.com'
# RECAPTCHA_SITE_KEY = '6LfnWmApAAAAAGaYFMRi2kRQffhQ7iUNuNq_yIak'
# RECAPTCHA_SECRET_KEY = '6LfnWmApAAAAAEB8Cp9GJmA11ytA-cmSZNjiRRth'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail0.godjango.dev'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sendertest@godjango.dev'
EMAIL_HOST_PASSWORD = 'Acl*123_2023*'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIAFILES_DIRS = (os.path.join(BASE_DIR, 'media'),)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APPEND_SLASH=True
JAZZMIN_SETTINGS = {
    "site_title": "Library Admin",
    "site_header": "Library",
    "site_brand": "Library",
    # "site_logo": "books/img/logo.png",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to the library",
    "copyright": "Acme Library Ltd",
    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "Main.Theme", "Main.Header", "Main.Carrousel",'Main.Service','Main.AboutUs','Main.Track',"Main.ReviewSection","Main.ContactUS","Main.Footer","Main.Suscribe"],
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "admin",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "Main.Theme": 'fas fa-magic',
        "Main.Header": 'fas fa-edit',
        "Main.Carrousel": 'fas fa-certificate',
        "Main.Service": 'fas fa-cog',
        "Main.AboutUs": 'fas fa-book',
        "Main.Track": 'fas fa-search',
        "Main.ReviewSection": 'fas fa-tasks',
        "Main.ContactUS": 'fas fa-phone',
        "Main.Footer": 'fas fa-bookmark',
        "Main.Suscribe": 'fas fa-user-plus',
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible",
                                    "auth.group": "vertical_tabs",
                                    "Main.Carrousel": "horizontal_tabs"
                                    },
    "language_chooser": False,
}