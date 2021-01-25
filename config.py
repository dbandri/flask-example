import os

class Config(object):
	DEBUG = False
	SECRET_KEY = 'my_secret_key'

class proConfig(Config):
	ENV = 'production'
	DEBUG = False
		
class devConfig(Config):
	ENV = 'development'
	DEBUG = True

class testConfig(Config):
	DEBUG = True
	TESTING = True
		