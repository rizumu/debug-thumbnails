"""
Django settings for thumbnail project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*vku$yu5!#0)r=vump1s1c*)fpk4@9r&t&4xt_eyrytx)z3*2*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "thumbnail", "templates"),
]

ALLOWED_HOSTS = []

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cumulus',
    'imagekit',

    'thumbnail.things',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'thumbnail.urls'

WSGI_APPLICATION = 'thumbnail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


DEFAULT_FILE_STORAGE = "cumulus.storage.SwiftclientStorage"

# these are the default cumulus settings
CUMULUS = {
    "API_KEY": os.environ.get("CUMULUS_API_KEY", None),
    'AUTH_URL': 'us_authurl',
    'REGION': 'DFW',
    'CNAMES': None,
    'CONTAINER': 'cumulus-content-tests',
    'CONTAINER_URI': None,
    'CONTAINER_SSL_URI': None,
    'STATIC_CONTAINER': 'cumulus-static-tests',
    'SERVICENET': False,
    'TIMEOUT': 5,
    'TTL': 600,
    'USE_SSL': False,
    "USERNAME": os.environ.get("CUMULUS_USERNAME", None),
    'INCLUDE_LIST': [],
    'EXCLUDE_LIST': [],
    'HEADERS': {},
    'GZIP_CONTENT_TYPES': [],
    'USE_PYRAX': True,
}

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = "imagekit.cachefiles.strategies.Optimistic"
IMAGEKIT_DEFAULT_FILE_STORAGE = "cumulus.storage.SwiftclientStorage"
