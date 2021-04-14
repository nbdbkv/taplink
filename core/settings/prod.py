import environ
env = environ.Env()


SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')

DATABASES = {'default': env.db('DATABASE_URL')}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
