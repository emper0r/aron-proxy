from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import os

ALLOWED_HOSTS = ['*']
DEBUG = False
DEFAULT_FROM_EMAIL = 'no-reply@domain.tld'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DHCP_CONF = '/etc/dhcp/dhcpd.conf'
LANGUAGE_CODE = 'it-it'
NETWORK_CONF = '/etc/network/interfaces'
ROOT_URLCONF = 'web.urls'
SECRET_KEY = ''
SERVER_LIC = ''
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SQUID_CONF = '/etc/squid/squid.conf'
SQUID_DIR = '/etc/squid/'
FIREHOL_DIR = '/etc/firehol/'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'web.wsgi.application'
SNMP = 'public'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Aron Proxy',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'SHOW_REQUIRED_ASTERISK': True,
    'MENU_OPEN_FIRST_CHILD': True,
    'LIST_PER_PAGE': 20,
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aron',
        'USER': 'aron',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'License',
    'Proxy',
    'Network',
    'Routing',
    'Configurazione',
    'DashBoard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

ADMINS = (
  ('Admin', 'user@domain.tld'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
