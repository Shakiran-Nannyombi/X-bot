import random
from .generators.educational import EducationalGenerator
from .generators.project import ProjectGenerator
from .generators.career import CareerGenerator
from .generators.resources import ResourceGenerator
from .generators.challenge import ChallengeGenerator
from .generators.motivational import MotivationalGenerator
from .generators.engagement import EngagementGenerator
from .generators.trending import TrendingGenerator
from .generators.reply import ReplyGenerator
from .generators.meme import MemeGenerator

class ContentGenerator:
    """Main content generator that coordinates all content types"""
    
    def __init__(self):
        self.generators = {
            'educational': EducationalGenerator(),
            'project': ProjectGenerator(),
            'career': CareerGenerator(),
            'resources': ResourceGenerator(),
            'challenge': ChallengeGenerator(),
            'motivational': MotivationalGenerator(),
            'engagement': EngagementGenerator(),
            'trending': TrendingGenerator(),
            'reply': ReplyGenerator(),
            'meme': MemeGenerator()
        }
    
    def generate(self, content_type, topic=None):
        """Generate content based on type and optional topic"""
        if content_type not in self.generators:
            content_type = 'educational'  # Default fallback
        
        generator = self.generators[content_type]
        return generator.generate(topic)
    
    def get_available_types(self):
        """Get list of available content types"""
        return list(self.generators.keys())
