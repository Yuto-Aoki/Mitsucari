import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'qboard_proj',
#         'USER': 'Mitsucari',
#         'PASSWORD': 'xxxxxxxx',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mitsukari_db', #DB名
        'USER': 'mitsukari',
        'HOST': 'mitsucari-app',
        'PASSWORD': 'mitsukari_pass', 
        'PORT': '5432'
    }
}

DEBUG = True