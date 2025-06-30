import random
from .base import BaseGenerator

class CareerGenerator(BaseGenerator):
    """Generate career advice content"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "💼 Career tip for aspiring developers:\n\n{tip}\n\n{explanation}\n\nRemember: {encouragement}\n\nWhat's your best career advice? 👇",
            "🎯 Breaking into tech? Here's what I wish I knew:\n\n1. {advice1}\n2. {advice2}\n3. {advice3}\n\nYour journey is unique. What worked for you? 🚀",
            "📚 Learning path for {field}:\n\nWeek 1-2: {step1}\nWeek 3-4: {step2}\nWeek 5-6: {step3}\nWeek 7-8: {step4}\n\nConsistent progress > perfect plans! 💪",
            "🔥 Unpopular opinion about tech careers:\n\n{opinion}\n\n{reasoning}\n\nAgree or disagree? Let's discuss! 🤔",
            "⚡ Quick wins for your tech career:\n\n✅ {win1}\n✅ {win2}\n✅ {win3}\n\nWhich one will you try this week? 🎯"
        ]
        
        self.career_data = {
            'tips': [
                'Build projects, not just tutorials',
                'Network genuinely, not transactionally',
                'Learn in public and document your journey',
                'Focus on problem-solving, not just syntax',
                'Contribute to open source early'
            ],
            'explanations': [
                'Projects show you can apply knowledge to solve real problems.',
                'Authentic relationships lead to better opportunities than cold outreach.',
                'Sharing your learning process helps others and builds your reputation.',
                'Employers care more about your thinking process than memorized code.',
                'It demonstrates collaboration skills and gives you real-world experience.'
            ],
            'encouragements': [
                'Everyone starts somewhere!',
                'Your unique background is an asset!',
                'Consistency beats intensity!',
                'Progress, not perfection!',
                'You belong in tech!'
            ],
            'fields': ['Data Science', 'Web Development', 'Machine Learning', 'DevOps', 'Mobile Development'],
            'opinions': [
                'You don\'t need a CS degree to be a great developer',
                'Bootcamps can be more practical than university',
                'Soft skills matter more than technical skills',
                'Remote work makes you a better developer',
                'Side projects are more valuable than certifications'
            ]
        }
    
    def generate(self, topic=None):
        """Generate career advice content"""
        template = self.get_random_template()
        data = self.career_data
        
        return template.format(
            tip=random.choice(data['tips']),
            explanation=random.choice(data['explanations']),
            encouragement=random.choice(data['encouragements']),
            advice1=random.choice(data['tips']),
            advice2=random.choice(data['tips']),
            advice3=random.choice(data['tips']),
            field=random.choice(data['fields']),
            step1='Learn fundamentals and basic syntax',
            step2='Build your first project',
            step3='Add complexity and new features',
            step4='Deploy and share your work',
            opinion=random.choice(data['opinions']),
            reasoning='Experience and problem-solving ability matter more than credentials.',
            win1='Update your LinkedIn with recent projects',
            win2='Engage with tech communities online',
            win3='Write about what you\'re learning'
        )
