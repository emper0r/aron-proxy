from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import os

ALLOWED_HOSTS = ['aron.ctimeapps.it']
DEBUG = False
DEFAULT_FROM_EMAIL = 'no-reply@aron.ctimeapps.it'
DG_DOMAIN = '/etc/dansguardian/lists/bannedsitelist'
DG_URL = '/etc/dansguardian/lists/bannedurllist'
DHCP_CONF = '/etc/dhcp/dhcpd.conf'
LANGUAGE_CODE = 'it-it'
NETWORK_CONF = '/etc/network/interfaces'
ROOT_URLCONF = 'web.urls'
SECRET_KEY = 'xz)*53&2z7w_-g_eajchp8p&*m1!9c*synd!^p-z4v9qdb*g%!'
SERVER_LIC = 'http://aron.ctimeapps.it:9090/'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SQUID_CONF = '/etc/squid3/squid.conf'
SQUID_DIR = '/etc/squid3/'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_L10N = True
USE_TZ = True
VEXIM_GID = 999
VEXIM_MAILHOME = '/srv/vmail/'
VEXIM_MAXMSGSIZE = 10485760
VEXIM_QUOTA = 1073741824
VEXIM_SA_TAG = 5
VEXIM_SA_REFUSE = 10
VEXIM_TYPE = 'local'
VEXIM_UID = 999
WSGI_APPLICATION = 'web.wsgi.application'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aron',
        'USER': 'aron',
        'PASSWORD': 'PasswordOfFantasy',
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
    'Internet',
    'Posta',
    'Network',
    'Statistics',
    'django_tables2',
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
 'django.contrib.auth.hashers.MD5PasswordHasher',
 'django.contrib.auth.hashers.PBKDF2PasswordHasher',
 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
 'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
 'django.contrib.auth.hashers.BCryptPasswordHasher',
 'django.contrib.auth.hashers.SHA1PasswordHasher',
 'django.contrib.auth.hashers.CryptPasswordHasher',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
