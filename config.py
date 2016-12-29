import os.path

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SERVER = 'smtps.bol.com.br'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TSL = False
MAIL_USERNAME = 'ronistonejunior@bol.com.br'
MAIL_PASSWORD = 'indiov1997'

SECRET_KEY = 'a1s2d3dw4q5e6t7x8p9ç0'