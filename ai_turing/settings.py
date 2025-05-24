from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-chatbot'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'chatbot',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'ai_turing.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'chatbot/templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [],
    },
}]

WSGI_APPLICATION = 'ai_turing.wsgi.application'
STATIC_URL = '/static/'
