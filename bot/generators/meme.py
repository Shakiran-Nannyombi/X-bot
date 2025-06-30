import random
from .base import BaseGenerator

class MemeGenerator(BaseGenerator):
    """Generate meme concepts for developers"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "🎭 Meme idea: Drake pointing meme\n\n❌ Writing documentation\n✅ Commenting 'TODO: write docs later'",
            "😅 Meme concept: Distracted boyfriend\n\nBoyfriend: Me\nGirlfriend: Current project\nOther woman: New shiny framework",
            "🔥 Meme template: This is fine dog\n\n'Everything is working in production'\n*10 error alerts in Slack*",
            "💀 Meme idea: Expanding brain\n\n1. console.log for debugging\n2. Using debugger\n3. Writing unit tests\n4. Rubber duck debugging",
            "🎪 Meme concept: Two buttons\n\nButton 1: Fix the bug properly\nButton 2: Add another if statement\n\n*Sweating guy choosing button 2*"
        ]
    
    def generate(self, topic=None):
        """Generate meme concept"""
        return self.get_random_template()
