import random
from .base import BaseGenerator

class ResourceGenerator(BaseGenerator):
    """Generate resource sharing content"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "📚 Free resources for learning {topic}:\n\n🔗 {resource1}\n🔗 {resource2}\n🔗 {resource3}\n\nBookmark this thread! Which one will you try first? 👇",
            "🎁 Curated list: Best {topic} tools (all free!):\n\n• {tool1} - {description1}\n• {tool2} - {description2}\n• {tool3} - {description3}\n\nWhat's your favorite {topic} tool? 🛠️",
            "💡 {topic} cheat sheet:\n\n{tip1}\n{tip2}\n{tip3}\n\nSave this for later! What would you add? 📝"
        ]
        
        self.resources_data = {
            'Python': {
                'resources': ['Python.org official tutorial', 'Automate the Boring Stuff', 'Real Python articles'],
                'tools': ['VS Code', 'Jupyter Notebooks', 'PyCharm Community'],
                'descriptions': ['Free, powerful code editor', 'Interactive coding environment', 'Full-featured Python IDE'],
                'tips': ['Use virtual environments for every project', 'Learn list comprehensions early', 'Master the debugger']
            },
            'JavaScript': {
                'resources': ['MDN Web Docs', 'JavaScript.info', 'FreeCodeCamp'],
                'tools': ['VS Code', 'Chrome DevTools', 'Node.js'],
                'descriptions': ['Best code editor for JS', 'Debug and inspect web apps', 'Run JavaScript everywhere'],
                'tips': ['Understand async/await deeply', 'Learn array methods well', 'Master the event loop']
            },
            'Data Science': {
                'resources': ['Kaggle Learn', 'Coursera Data Science', 'Towards Data Science'],
                'tools': ['Jupyter Lab', 'Google Colab', 'Pandas'],
                'descriptions': ['Advanced notebook interface', 'Free cloud notebooks', 'Data manipulation library'],
                'tips': ['Start with exploratory data analysis', 'Visualize before modeling', 'Clean data is crucial']
            }
        }
    
    def generate(self, topic=None):
        """Generate resource sharing content"""
        topic = topic or random.choice(list(self.resources_data.keys()))
        data = self.resources_data[topic]
        template = self.get_random_template()
        
        return template.format(
            topic=topic,
            resource1=random.choice(data['resources']),
            resource2=random.choice(data['resources']),
            resource3=random.choice(data['resources']),
            tool1=random.choice(data['tools']),
            tool2=random.choice(data['tools']),
            tool3=random.choice(data['tools']),
            description1=random.choice(data['descriptions']),
            description2=random.choice(data['descriptions']),
            description3=random.choice(data['descriptions']),
            tip1=random.choice(data['tips']),
            tip2=random.choice(data['tips']),
            tip3=random.choice(data['tips'])
        )
