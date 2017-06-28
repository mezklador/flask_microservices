# project/config.py


class BaseConfig:
    """Base configuration class"""
    DEBUG = False
    TESTING = False


class DevConfig(BaseConfig):
    """Development configuration class"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration class"""
    DEBUG = True
    TESTING = True


class ProdConfig(BaseConfig):
    """Production configuration class"""
    DEBUG = False
