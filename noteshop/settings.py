
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d76@!p902rrjwg8i0_@ma_@5na7wlt^4nt=mnopzz4jn4p)z7w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ['34.107.48.118']
=======
ALLOWED_HOSTS = []
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Приложения 
    'products',
<<<<<<< HEAD

    #Lib
    'rest_framework',
    'likes.apps.LikesConfig',
    'Order',

=======
    #Lib
    'rest_framework'
    
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
    # Accounts
    'account',

    ## Libraries
    # Token Authentication
<<<<<<< HEAD
    'rest_framework.authtoken',
    'django_filters',

=======
    'rest_framework',
    'rest_framework.authtoken',
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a


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

ROOT_URLCONF = 'noteshop.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'noteshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'noteshop',
        'USER': 'admin',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '',
    }
}


AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',

)

=======
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'noteshop',
        # 'USER': 'alisher',
        'USER': 'baiel',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': 5432,
        
    }
}

>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'noteshop/static')
]
=======

>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a

MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
<<<<<<< HEAD
}

=======

}


>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
AUTH_USER_MODEL = 'account.User'

# Email configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

# свой email
EMAIL_HOST_USER = 'noteshop.bishkek@gmail.com'
<<<<<<< HEAD
EMAIL_HOST_PASSWORD = '456545654'
=======
EMAIL_HOST_PASSWORD = '456545654'
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
