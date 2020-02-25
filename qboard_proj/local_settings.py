import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '0m2_&-(19k4*(rqwn5yx-sn21t&j07q@#u8+=6#u0q6w4bori0'

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
        'PASSWORD': 'localhost', 
        'PORT': '5432'
    }
}

DEBUG = True