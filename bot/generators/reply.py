import random
from .base import BaseGenerator

class ReplyGenerator(BaseGenerator):
    """Generate reply suggestion content"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "💬 Great discussion starter reply:\n\n'{reply}'\n\nUse this when you want to add value to tech conversations! 🎯",
            "🤝 Thoughtful engagement reply:\n\n'{reply}'\n\nPerfect for building meaningful connections in tech communities! 💪",
            "🧠 Insightful follow-up:\n\n'{reply}'\n\nUse this to deepen technical discussions! 🚀",
            "💡 Value-adding response:\n\n'{reply}'\n\nGreat for showing expertise while being helpful! ✨"
        ]
        
        self.replies = [
            "Great point! I've found that [specific experience] also applies here. Have you tried [suggestion]?",
            "This reminds me of [related concept]. The key difference is [insight]. What's been your experience?",
            "Interesting perspective! I'd add that [additional point] is also worth considering. Thoughts?",
            "Love this! For anyone starting out, I'd recommend [practical tip] as a first step.",
            "Exactly! And for those who want to dive deeper, [resource/tool] is incredibly helpful.",
            "This is why I always [best practice]. It's saved me countless hours of debugging!",
            "Great thread! One thing I'd add: [insight] - it's often overlooked but crucial.",
            "Spot on! I learned this the hard way when [brief story]. Now I always [lesson learned]."
        ]
    
    def generate(self, topic=None):
        """Generate reply suggestion content"""
        template = self.get_random_template()
        return template.format(reply=random.choice(self.replies))
