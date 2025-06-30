import random
from .base import BaseGenerator

class TrendingGenerator(BaseGenerator):
    """Generate trending topic content"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "🔥 Trending in tech: {topic}\n\n{insight}\n\nMy take: {opinion}\n\nWhat's your experience with {topic}? 👇",
            "📈 {topic} is gaining traction!\n\nWhy it matters:\n• {reason1}\n• {reason2}\n• {reason3}\n\nWorth learning? What do you think? 🤔",
            "⚡ Hot take on {topic}:\n\n{hot_take}\n\n{explanation}\n\nAgree or disagree? Let's discuss! 🔥"
        ]
        
        self.trending_topics = [
            'AI-powered coding assistants',
            'WebAssembly adoption',
            'Serverless architecture',
            'Low-code/no-code platforms',
            'Edge computing',
            'Rust programming language',
            'GraphQL vs REST',
            'Micro-frontends',
            'DevOps automation',
            'Quantum computing'
        ]
    
    def generate(self, topic=None):
        """Generate trending topic content"""
        topic = topic or random.choice(self.trending_topics)
        template = self.get_random_template()
        
        return template.format(
            topic=topic,
            insight=f'{topic} is changing how we approach development',
            opinion='It has potential but needs careful implementation',
            reason1='Improves developer productivity',
            reason2='Reduces complexity',
            reason3='Better performance',
            hot_take=f'{topic} is overhyped but still valuable',
            explanation='Like any new tech, it solves specific problems well'
        )
