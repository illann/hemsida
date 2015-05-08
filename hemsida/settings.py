"""
Django settings for hemsida project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h*o@oj0o0^h$z8dsxsm419n^qpbhw79m!1yt^u-vj!poe5rp4u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'article',
	'south',
	#'notification',
	#'custom_user',
	'userprofile',
	#'offert',
	'crispy_forms',
)

######################### AUTH for Custom user ############################

#AUTH_USER_MODEL = "custom_user.CustomUser"

#AUTHENTICATION_BACKENDS = ('custom_user.backends.CustomUserAuth',)

###########################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hemsida.urls'

WSGI_APPLICATION = 'hemsida.wsgi.application'


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

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	('assets', os.path.join(BASE_DIR, "static")),
	#"D:/Django/hemsida/static",
	#os.path.join(PROJECT_PATH, "static"),
)

STATICFILES_FINDERS = (
     'django.contrib.staticfiles.finders.FileSystemFinder',
     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT =  os.path.join(BASE_DIR, 'static/')

 

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),
				'/Django/hemsida/article/templates',)
				
LOGIN_URL = '/accounts/login/'


"""
DELETE_MESSAGE = 50

MESSAGE_TAGS = {
    DELETE_MESSAGE : 'deleted',

"""	
	
TEMPLATE_CONTEXT_PROCESSORS = {
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',  
    'django.contrib.messages.context_processors.messages',
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mecotivab@gmail.com'
EMAIL_HOST_PASSWORD = 'mecotivgbg'
 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER