import os

# Try to import SECRET_KEY from secret.py in development
try:
    from .secret import SECRET_KEY
except ImportError:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

class Config:
    """Base configuration class"""
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    SECRET_KEY = SECRET_KEY
    
    # App settings
    APP_NAME = "X Growth Bot"
    APP_VERSION = "1.0.0"
    
    # Content generation settings
    DEFAULT_CONTENT_TYPE = 'educational'
    MAX_CONTENT_LENGTH = 280
    
    # Notification settings
    DEFAULT_NOTIFICATION_TIMES = {
        'morning': '09:00',
        'afternoon': '13:30',
        'evening': '20:00'
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    def __init__(self):
        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY environment variable must be set in production")

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
