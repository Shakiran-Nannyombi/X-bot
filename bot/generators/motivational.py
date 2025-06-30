import random
from .base import BaseGenerator

class MotivationalGenerator(BaseGenerator):
    """Generate motivational content for developers"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "🚀 That bug you've been fighting for hours?\n\nIt's not a reflection of your skills.\nIt's a puzzle waiting to be solved.\n\nTake a break. Come back fresh. You've got this! 💪",
            "💭 Reminder: Every expert was once a beginner.\n\nThat senior dev you admire? They googled 'how to center a div' too.\n\nKeep learning, keep growing. 🌱",
            "🔥 Your code doesn't have to be perfect.\nIt has to work.\n\nPerfection is the enemy of progress.\nShip it, learn from it, improve it. 🚢",
            "⚡ Imposter syndrome hitting hard?\n\nYou belong here.\nYour perspective matters.\nYour code makes a difference.\n\nKeep pushing forward! 🎯",
            "🌟 Failed technical interview?\nBug in production?\nProject didn't work out?\n\nThese aren't failures.\nThey're data points.\nThey're making you stronger. 📈"
        ]
    
    def generate(self, topic=None):
        """Generate motivational content"""
        return self.get_random_template()
