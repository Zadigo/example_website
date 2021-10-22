import os
import datetime

import stripe
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONT_DIR = os.path.join(BASE_DIR, 'front')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'drd&f=j9iq^_#0*r1*9g87^h7k5h3mny%b!k-%43ldlyvn7=20'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.ngrok.io']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'corsheaders',
    'debug_toolbar',
    'social_django',
    'graphene_django',
    'django_filters',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'graphql_auth',

    'company',
    'analytics',
    'dashboard',
    'accounts',
    'legal',
    'hero',
    'nodesplus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'example_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(FRONT_DIR, 'dist')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                'legal.context_processors.legal',
                'company.context_processors.company',
                'hero.context_processors.hero'
            ],
            'libraries': {
                'utils': 'accounts.templatetags.utils',
                'nodes_plus': 'nodesplus.templatetags.nodes_plus',

                'analytics_tags': 'analytics.templatetags.analytics_tags'
            }
        },
    },
]

WSGI_APPLICATION = 'example_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(FRONT_DIR, 'dist/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Authentication

AUTH_USER_MODEL = 'accounts.MyUser'

AUTHENTICATION_BACKENDS = [
    # 'graphql_jwt.backends.JSONWebTokenBackend',
    'graphql_auth.backends.GraphQLAuthBackend',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.open_id.OpenIdAuth',
    # 'social_core.backends.google.GoogleOpenId',
    # 'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    'accounts.backends.EmailAuthenticationBackend'
]


# Social Django

LOGIN_URL = 'accounts:login'

LOGOUT_URL = 'accounts:logout'

LOGIN_REDIRECT_URL = 'accounts:profile:home'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')


# LOGGING

# LOGGING = {
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'werkzeug': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }


# GMAIL

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_USE_LOCALTIME = True


# AMAZON S3

# AWS_ACCESS_KEY_ID = ''

# AWS_SECRET_ACCESS_KEY = ''

# AWS_STORAGE_BUCKET_NAME = ''

# AWS_S3_REGION_NAME = ''

# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400'
# }

# AWS_QUERYSTRING_AUTH = False

# AWS_DEFAULT_ACL = None

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_LOCATION = 'nawoka/static'

# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

# STATIC_ROOT = 'staticfiles'

# AWS_MEDIA_LOCATION = ''

# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Debugging

INTERNAL_IPS = [
    '127.0.0.1'
]


# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.environ.get('CACHE_FILE_LOCATION', os.path.join(BASE_DIR, 'cache'))
    },
    'inmemcache': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211'
    }
}


# Languages

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('Français')),
]


# Stripe

STRIPE_TEST_KEYS = []

STRIPE_LIVE_KEYS = []

try:
    if DEBUG:
        stripe.api_key = STRIPE_TEST_KEYS[0]
    else:
        stripe.api_key = STRIPE_LIVE_KEYS[0]
except:
    pass


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# HERO

HERO = {
    'hero_image': 'https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg?cs=srgb&dl=pexels-moose-photos-1036623.jpg&fm=jpg'
}

LEGAL = {}

ENTERPRISE = {
    'company_description': 'This is a simple description',
    'contact': {
        'address': '15, rue du Château',
        'zip_code': '75001 Paris, France',
        'emails': {
            'main': 'info@monsite.fr'
        },
        'telephone': {
            'main': '01 23 45 67 89'
        }
    },
    'link_to_app_store': 'http://',
    'link_to_play_store': 'http://',
    'socials': [
        {'alt': 'Facebook', 'url': 'https://www.facebook.com/mdbootstrap'},
        {'alt': 'Github', 'url': 'https://github.com/Zadigo'}
    ],
}


# CORS

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_REGEX_WHITELIST = [
    r'^https?\:\/\/localhost\:808\d{1}$',
    r'^https?\:\/\/192\.168\.0\.\d{3}\:8080$'
]

CSRF_TRUSTED_ORIGINS = [
    'localhost:8080',
    '192.168.0.103:8080',
]

# GraphQL

GRAPHQL_AUTH = {
    'LOGIN_ALLOWED_FIELDS': 'email',
    'UPDATE_MUTATION_FIELDS': ['firstname', 'lastname'],
    'SEND_ACTIVATION_EMAIL': False,
    'REGISTER_MUTATION_FIELDS': {
        'email': 'String'
    }
}

GRAPHQL_JWT = {
    # 'JWT_PAYLOAD_HANDLER': 'app.utils.jwt_payload',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=5),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_SECRET_KEY': os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY),
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_ANY_CLASSES': [
        'graphql_auth.mutations.Register',
        # 'graphql_auth.mutations.Register',
        # 'graphql_auth.mutations.VerifyAccount',
        # 'graphql_auth.mutations.ResendActivationEmail',
        # 'graphql_auth.mutations.SendPasswordResetEmail',
        # 'graphql_auth.mutations.PasswordReset',
        # 'graphql_auth.mutations.ObtainJSONWebToken',
        # 'graphql_auth.mutations.VerifyToken',
        # 'graphql_auth.mutations.RefreshToken',
        # 'graphql_auth.mutations.RevokeToken',
        # 'graphql_auth.mutations.VerifySecondaryEmail'
    ]
}

GRAPHENE = {
    'SCHEMA': 'graph.schema.schema',
    'ATOMIC_MUTATIONS': True,
    'MIDDLEWARE': {
        'graphql_jwt.middleware.JSONWebTokenMiddleware'
    }
}


# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
