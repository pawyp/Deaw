from os.path import isfile
from envparse import env
import logging


log = logging.getLogger('app')
log.setLevel(logging.DEBUG)

f = logging.Formatter('[L:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', datefmt = '%d-%m-%Y %H:%M:%S')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(f)
log.addHandler(ch)

if isfile('.env'):
    env.read_envfile('.env')

DEBUG = env.bool('DEBUG', default=False)

SITE_HOST = '127.0.0.1'
SITE_PORT = 8000

MONGO_HOST = '127.0.0.1:27017'
MONGO_DB_NAME = 'servtest'
import fernet, base64
# SITE_HOST = env.str('HOST')
# SITE_PORT = env.int('PORT')
fernet_key = fernet.Fernet.generate_key()
SECRET_KEY = base64.urlsafe_b64decode(fernet_key)
# SECRET_KEY = fernet.Fernet.generate_key()

# MONGO_HOST = env.str('MONGO_HOST')
# MONGO_DB_NAME = env.str('MONGO_DB_NAME')

MESSAGE_COLLECTION = 'messages'
USER_COLLECTION = 'users'
