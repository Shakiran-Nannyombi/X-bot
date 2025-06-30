import random
from .base import BaseGenerator

class EducationalGenerator(BaseGenerator):
    """Generate educational content for developers and data scientists"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "🧵 Thread: {topic} explained in simple terms:\n\n1. {point1}\n2. {point2}\n3. {point3}\n\nWhat would you add? 👇",
            "💡 Quick {topic} tip:\n\n{tip}\n\nThis saved me hours of debugging. What's your go-to {topic} trick?",
            "🔥 {topic} best practice:\n\n{practice}\n\nIgnore this at your own risk! 😅\n\n#coding #programming",
            "📚 Learning {topic}? Start here:\n\n✅ {step1}\n✅ {step2}\n✅ {step3}\n\nWhat was your biggest {topic} challenge?",
            "⚡ {topic} performance tip:\n\n{performance_tip}\n\nYour users will thank you! 🚀"
        ]
        
        self.topics_data = {
            'Python': {
                'points': ['List comprehensions save memory', 'Use f-strings for formatting', 'Virtual environments are essential'],
                'tips': ['Use enumerate() instead of range(len())', 'Leverage defaultdict for cleaner code', 'Profile before optimizing'],
                'practices': ['Always use type hints', 'Write docstrings for functions', 'Follow PEP 8 style guide'],
                'steps': ['Master the basics first', 'Build projects, not just tutorials', 'Read other people\'s code'],
                'performance_tips': ['Use generators for large datasets', 'Cache expensive function calls', 'Choose the right data structure']
            },
            'JavaScript': {
                'points': ['Async/await makes code readable', 'Destructuring simplifies assignments', 'Arrow functions are concise'],
                'tips': ['Use const by default, let when needed', 'Avoid var completely', 'Learn array methods like map, filter, reduce'],
                'practices': ['Always handle errors properly', 'Use meaningful variable names', 'Keep functions small and focused'],
                'steps': ['Understand the event loop', 'Master DOM manipulation', 'Learn modern ES6+ features'],
                'performance_tips': ['Debounce expensive operations', 'Use event delegation', 'Minimize DOM queries']
            },
            'Data Science': {
                'points': ['Clean data is more important than fancy models', 'Visualization reveals hidden patterns', 'Domain knowledge beats algorithms'],
                'tips': ['Start with exploratory data analysis', 'Validate your assumptions with data', 'Document your data pipeline'],
                'practices': ['Version control your datasets', 'Reproducible analysis is key', 'Always validate your models'],
                'steps': ['Learn statistics fundamentals', 'Master pandas and numpy', 'Practice on real datasets'],
                'performance_tips': ['Vectorize operations in pandas', 'Use appropriate data types', 'Sample large datasets for exploration']
            }
        }
    
    def generate(self, topic=None):
        """Generate educational content"""
        if not topic:
            topic = random.choice(list(self.topics_data.keys()))
        
        template = self.get_random_template()
        data = self.topics_data.get(topic, self.topics_data['Python'])
        
        return template.format(
            topic=topic,
            point1=random.choice(data['points']),
            point2=random.choice(data['points']),
            point3=random.choice(data['points']),
            tip=random.choice(data['tips']),
            practice=random.choice(data['practices']),
            step1=random.choice(data['steps']),
            step2=random.choice(data['steps']),
            step3=random.choice(data['steps']),
            performance_tip=random.choice(data['performance_tips'])
        )
