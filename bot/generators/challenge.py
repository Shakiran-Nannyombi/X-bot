import random
from .base import BaseGenerator

class ChallengeGenerator(BaseGenerator):
    """Generate coding challenge content"""
    
    def __init__(self):
        super().__init__()
        self.templates = [
            "🧩 Daily coding challenge:\n\n{challenge}\n\nExample:\nInput: {input_example}\nOutput: {output_example}\n\nDrop your solution below! Any language welcome 👇\n\n#CodingChallenge",
            "⚡ Quick algorithm question:\n\n{question}\n\nThink you know the answer? Reply with:\n1. Your approach\n2. Time complexity\n3. Code snippet (optional)\n\nLet's learn together! 🚀",
            "🎯 Weekend coding puzzle:\n\n{puzzle}\n\nBonus points for:\n• Clean, readable code\n• Handling edge cases\n• Explaining your approach\n\nWho's up for the challenge? 💪"
        ]
        
        self.challenge_data = {
            'challenges': [
                'Write a function that finds the two numbers in an array that add up to a target sum',
                'Implement a function to reverse a string without using built-in methods',
                'Create a function that checks if a string is a palindrome',
                'Write a function to find the maximum element in a rotated sorted array',
                'Implement a function that merges two sorted arrays'
            ],
            'questions': [
                'What\'s the most efficient way to find duplicates in an array?',
                'How would you implement a LRU cache?',
                'What\'s the best approach for detecting cycles in a linked list?',
                'How do you find the kth largest element in an array?',
                'What\'s an efficient way to validate balanced parentheses?'
            ],
            'puzzles': [
                'Build a simple calculator that handles +, -, *, / operations',
                'Create a function that generates the Fibonacci sequence up to n terms',
                'Implement a basic hash table with collision handling',
                'Write a function that converts Roman numerals to integers',
                'Create a simple text-based tic-tac-toe game'
            ]
        }
    
    def generate(self, topic=None):
        """Generate coding challenge content"""
        template = self.get_random_template()
        data = self.challenge_data
        
        return template.format(
            challenge=random.choice(data['challenges']),
            input_example='[2, 7, 11, 15], target = 9',
            output_example='[0, 1] (indices of 2 and 7)',
            question=random.choice(data['questions']),
            puzzle=random.choice(data['puzzles'])
        )
