import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
    b'\x18[\xa9:l\x83\xedB\x1aQD!l\x82-\xdb'

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment' }