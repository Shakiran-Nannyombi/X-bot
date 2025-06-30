import random
from .base import BaseGenerator

class ProjectGenerator(BaseGenerator):
    """Generate project highlight content"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "🚀 Just shipped: {project_name}\n\n✨ What it does: {description}\n🛠️ Built with: {tech_stack}\n📊 Results: {results}\n\n{cta}\n\n#{hashtag1} #{hashtag2}",
            "💡 Weekend project update: {project_name}\n\n{problem_solved}\n\nTech stack:\n• {tech1}\n• {tech2}\n• {tech3}\n\nNext steps: {next_steps}\n\nThoughts? 👇",
            "🔥 Open source contribution: {contribution}\n\nWhy this matters:\n{impact}\n\nWant to contribute too? Here's how:\n{how_to_contribute}\n\n#OpenSource #Coding",
            "📈 Project milestone: {milestone}\n\n{journey_description}\n\nKey learnings:\n1. {learning1}\n2. {learning2}\n3. {learning3}\n\nWhat's your biggest project learning? 🤔"
        ]
        
        self.project_data = {
            'project_names': ['TaskFlow API', 'DataViz Dashboard', 'ML Predictor', 'Code Analyzer', 'DevTools Extension'],
            'descriptions': ['Streamlines workflow automation', 'Interactive data visualization platform', 'Predictive analytics tool', 'Code quality assessment tool', 'Productivity booster for developers'],
            'tech_stacks': ['Python + FastAPI + PostgreSQL', 'React + D3.js + Node.js', 'Python + Scikit-learn + Flask', 'JavaScript + AST parsing', 'JavaScript + Chrome APIs'],
            'results': ['50% faster task completion', '10x better data insights', '85% prediction accuracy', 'Reduced bugs by 30%', '2x developer productivity'],
            'ctas': ['Try it out and let me know what you think!', 'Would love your feedback!', 'Open to collaboration!', 'Star it if you find it useful!'],
            'contributions': ['Fixed memory leak in popular library', 'Added dark mode to open source tool', 'Improved documentation for beginners', 'Optimized database queries'],
            'impacts': ['Improves performance for 10k+ users', 'Better UX for night-time coding', 'Easier onboarding for new contributors', 'Faster queries save server costs']
        }
    
    def generate(self, topic=None):
        """Generate project highlight content"""
        template = self.get_random_template()
        data = self.project_data
        
        return template.format(
            project_name=random.choice(data['project_names']),
            description=random.choice(data['descriptions']),
            tech_stack=random.choice(data['tech_stacks']),
            results=random.choice(data['results']),
            cta=random.choice(data['ctas']),
            hashtag1=random.choice(['TechProject', 'BuildInPublic', 'SideProject']),
            hashtag2=random.choice(['Coding', 'Programming', 'WebDev']),
            problem_solved=f"Solving the '{random.choice(['data visualization', 'API performance', 'user authentication', 'code organization'])}' problem",
            tech1=random.choice(['React', 'Python', 'Node.js', 'PostgreSQL']),
            tech2=random.choice(['TypeScript', 'FastAPI', 'Redis', 'Docker']),
            tech3=random.choice(['Tailwind', 'Jest', 'GitHub Actions', 'AWS']),
            next_steps=random.choice(['Add user authentication', 'Improve performance', 'Add more features', 'Write documentation']),
            contribution=random.choice(data['contributions']),
            impact=random.choice(data['impacts']),
            how_to_contribute='Check the issues tab, pick a good first issue, and submit a PR!',
            milestone=random.choice(['1000 users!', '100 GitHub stars!', 'First paying customer!', 'Featured on Product Hunt!']),
            journey_description=random.choice(['Started as a weekend hack, now it\'s growing!', 'From idea to reality in 30 days', 'Community feedback shaped this project']),
            learning1=random.choice(['User feedback is invaluable', 'Start simple, iterate fast', 'Documentation matters']),
            learning2=random.choice(['Testing saves time later', 'Performance optimization is crucial', 'Community building takes time']),
            learning3=random.choice(['Open source is rewarding', 'Consistency beats perfection', 'Ship early, improve often'])
        )
