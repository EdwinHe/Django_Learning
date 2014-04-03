"""
Django settings for depot project.

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
SECRET_KEY = '6dr)wj+0b&87mun8t^36q@9&^#2!=s)&07z+0u$67v+ad&4l0@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
# 	'django.contrib.admin',
# 	'django.contrib.auth',
# 	'django.contrib.contenttypes',
	'django.contrib.sessions',
# 	'django.contrib.messages',
 	'django.contrib.staticfiles',
	'depotapp',
 	'rest_framework',  # REST Framework
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
# 	'django.middleware.common.CommonMiddleware',
# 	'django.middleware.csrf.CsrfViewMiddleware',
# 	'django.contrib.auth.middleware.AuthenticationMiddleware',
# 	'django.contrib.messages.middleware.MessageMiddleware',
# 	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'depot.urls'

WSGI_APPLICATION = 'depot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	'default': {
		## SQLite3
		#'ENGINE': 'django.db.backends.sqlite3',
		#'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

		## MySQL
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'django_depot',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': '127.0.0.1',
		'PORT': '',	
		
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/ACT'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'depot/templates')]
STATICFILES_DIRS  = (os.path.join(BASE_DIR, 'depot/static'),)


# REST Framework
REST_FRAMEWORK = {
	## Turn this on requires login
    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

# Trun this on to allow accessing request.session.ITEMS from template
#TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',)