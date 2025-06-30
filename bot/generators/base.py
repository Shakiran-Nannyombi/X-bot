import random
from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    """Base class for all content generators"""
    
    def __init__(self):
        self.templates = []
        self.data = {}
    
    @abstractmethod
    def generate(self, topic=None):
        """Generate content - must be implemented by subclasses"""
        pass
    
    def get_random_template(self):
        """Get a random template from available templates"""
        return random.choice(self.templates)
    
    def format_template(self, template, **kwargs):
        """Format template with provided data"""
        return template.format(**kwargs)
