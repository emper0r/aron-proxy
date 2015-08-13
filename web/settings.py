from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

SITE_ID = 1
SECRET_KEY = 'xz)*53&2z7w_-g_eajchp8p&*m1!9c*synd!^p-z4v9qdb*g%!'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['localhost']
ROOT_URLCONF = 'web.urls'
WSGI_APPLICATION = 'web.wsgi.application'
STATIC_URL = '/usr/local/src/aron-web/aron/static/'
LANGUAGE_CODE = 'it-it'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_L10N = True
USE_TZ = True
VEXIM_UID = 999
VEXIM_GID = 999
VEXIM_MAILHOME = '/srv/vmail/'
VEXIM_MAXMSGSIZE = 10485760
VEXIM_QUOTA = 1073741824
VEXIM_SA_TAG = 5
VEXIM_SA_REFUSE = 10
VEXIM_TYPE = 'local'
SQUID_DIR = '/etc/squid3/'
SQUID_CONF = '/etc/squid3/squid.conf'
DG_DOMAIN = '/etc/dansguardian/lists/bannedsitelist'
DG_URL = '/etc/dansguardian/lists/bannedurllist'
NETWORK_CONF = '/etc/network/interfaces'
DEFAULT_FROM_EMAIL = 'no-reply@aron.ctimeapps.it'

INSTALLED_APPS = (
    'suit',
    # 'material',
    # 'material.frontend',
    # 'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Internet',
    'Posta',
    'Network',
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

PASSWORD_HASHERS = (
 'django.contrib.auth.hashers.MD5PasswordHasher',
 'django.contrib.auth.hashers.PBKDF2PasswordHasher',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'material.frontend.context_processors.modules',
)

