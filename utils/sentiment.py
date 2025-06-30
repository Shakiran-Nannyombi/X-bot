"""
Sentiment analysis utility using TextBlob.
"""
from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze sentiment of the given text. Returns polarity and subjectivity."""
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity 