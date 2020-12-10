import os

class Config:
    """
    general configuration parent class
    """
   



class ProdConfig(Config):
    """
    production configuration child clas

    Args:
       config: The parent configuration class with general configuration settings
    """
    pass

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kadas36@localhost/pomodoro'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

    Args:
        Config: The parent configuration class with General configuration settings.
    """
    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig

config_options = {
'development':DevConfig,
'production':ProdConfig
}