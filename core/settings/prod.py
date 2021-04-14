import environ
env = environ.Env()


<<<<<<< HEAD
SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')

DATABASES = {'default': env.db('DATABASE_URL')}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
=======
SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG')

DATABASES = {'default': env.db('DATABASE_URL')}

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
>>>>>>> fe759124b250b6ed89b3c3ce0ed0ce91386ac312
