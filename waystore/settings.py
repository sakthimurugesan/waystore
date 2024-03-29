

from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import cloudinary_storage


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dfiyrqut1',
    'API_KEY': '327587213475877',
    'API_SECRET': '97VBYey4niCLGNgFucWURQlaxCo'
}
BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-@w$g+_=n9fu6eg+i&#h412anuq+g!=c^t@jdje0*^jcoav03&j'

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
    'store',
    'account',
    'orders_cart_wishlist',
    'cloudinary_storage',
    'cloudinary',
    'django_summernote',
    'easy_thumbnails',
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

ROOT_URLCONF = 'waystore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.context.custom_context',
                'account.context.getuser',
                'account.context.get_len_cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'waystore.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'waystore',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
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



STATIC_URL = 'static/'
STATIC_ROOT=BASE_DIR
STATICFILES_DIRS=[
    BASE_DIR/'static'
]
MEDIA_URL = '/media/'
X_FRAME_OPTIONS = 'SAMEORIGIN'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py

AUTH_USER_MODEL = 'account.CustomUser'
SESSION_ENGINE="django.contrib.sessions.backends.db"
SESSION_COOKIE_SECURE=True