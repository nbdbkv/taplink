import environ
env = environ.Env()


SECRET_KEY = env.str('SECRET_KEY', default='not secret)')

DEBUG = env.bool('DEBUG', default=True)

DATABASES = {
    'default': env.db(
        'DATABASE_URL', default='sqlite:///db.sqlite'
    )
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
