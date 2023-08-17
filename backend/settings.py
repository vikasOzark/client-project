"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l_p_p)&9b0#f@3_3b7@=@)4*k1ws=7(gtlr@o*=cl*v^e=x6a#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", "www.blackrokinvest.in", "blackrokinvest.in", "154.56.60.250", "172.20.10.11"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'authentication',
    'userprofile',
    'compressor'
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

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     "default" : {
#         "ENGINE" : "django.db.backends.postgresql",
#         "NAME" : "blackrokinvest_db",
#         "USER" : "blackrokinvest",
#         "PASSWORD" : "Blackrokinvest@1234##",
#         "HOST" : "127.0.0.1",              
#         "PORT" : "5432",
#         }
# }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

# STATIC_ROOT =  "root/blackrokinvest/static"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# COMPRESS_ROOT = BASE_DIR / 'static'

# COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.AppDirectoriesFinder',)

# STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',
#                         'django.contrib.staticfiles.finders.AppDirectoriesFinder',)
CSRF_TRUSTED_ORIGINS=["http://blackrokinvest.in", "https://blackrokinvest.in", "https://www.blackrokinvest.in"]
# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
LOGIN_URL = "login"

# Enable SSL by setting this to True
USE_SSL = True

# Paths to SSL certificate and private key files
SSL_CERTIFICATE_PATH = os.path.join(BASE_DIR, "nginx", "letsencrypt", "cert.pem")
SSL_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, "nginx", "letsencrypt", "key.pem")
CSRF_TRUSTED_ORIGINS = ["https://blackrokinvest.in", "https://wwww.blackrokinvest.in"]