
class Config(object):
	DEBUG = False
	SECRET_KEY = 'my_secret_key'

class proConfig(Config):
	ENV = 'production'
	DB_SERVER = '190.73.11.131'
		
class devConfig(Config):
	ENV = 'development'
	DEBUG = True

class testConfig(Config):
	TESTING = True
		