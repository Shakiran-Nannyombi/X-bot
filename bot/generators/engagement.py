import random
from .base import BaseGenerator

class EngagementGenerator(BaseGenerator):
    """Generate engagement-focused content"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "🤔 Quick poll: What's your biggest coding challenge right now?\n\nA) Debugging complex issues\nB) Learning new technologies\nC) Time management\nD) Imposter syndrome\n\nDrop your answer below! 👇",
            "💬 Controversial opinion:\n\n{opinion}\n\nChange my mind! What's your take? 🔥",
            "🎯 Fill in the blank:\n\nThe best advice I'd give to my past self starting in tech is:\n\n'_________________'\n\nWhat's yours?",
            "🚨 Red flag in code reviews:\n\n{red_flag}\n\nWhat red flags make you cringe? Share below! 😬",
            "⚖️ Tabs vs Spaces?\nVim vs VSCode?\nPython vs JavaScript?\n\nWhat's your pick and why? Let's settle this once and for all! 😄"
        ]
        
        self.opinions = [
            "Code comments are often a sign of bad code",
            "You don't need to know algorithms to be a good developer",
            "Bootcamps can be better than CS degrees for practical skills",
            "Remote work makes you a better developer",
            "AI will make developers more valuable, not less"
        ]
        
        self.red_flags = [
            "Functions longer than your screen",
            "Variable names like 'data', 'temp', 'x'",
            "No error handling anywhere",
            "Copy-pasted code everywhere",
            "Zero documentation or comments"
        ]
    
    def generate(self, topic=None):
        """Generate engagement content"""
        template = self.get_random_template()
        return template.format(
            opinion=random.choice(self.opinions),
            red_flag=random.choice(self.red_flags)
        )
