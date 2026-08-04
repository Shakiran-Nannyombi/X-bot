"""
Lightweight sentiment analysis (no NLTK/TextBlob).
Returns polarity and subjectivity in roughly the same ranges as TextBlob.
"""

POSITIVE = {
    "amazing", "awesome", "best", "brilliant", "excellent", "fantastic",
    "good", "great", "happy", "love", "loved", "nice", "positive",
    "success", "successful", "win", "wonderful", "excited", "helpful",
    "impressive", "outstanding", "perfect", "proud", "thank", "thanks",
}

NEGATIVE = {
    "awful", "bad", "broken", "bug", "crash", "fail", "failed", "failure",
    "hate", "horrible", "issue", "negative", "poor", "problem", "sad",
    "terrible", "worst", "angry", "annoying", "disappointing", "error",
    "frustrated", "slow", "useless", "wrong",
}


def analyze_sentiment(text):
    """Analyze sentiment of the given text. Returns polarity and subjectivity."""
    if not text or not str(text).strip():
        return 0.0, 0.0

    tokens = [
        "".join(ch for ch in word.lower() if ch.isalnum())
        for word in str(text).split()
    ]
    tokens = [t for t in tokens if t]
    if not tokens:
        return 0.0, 0.0

    pos = sum(1 for t in tokens if t in POSITIVE)
    neg = sum(1 for t in tokens if t in NEGATIVE)
    scored = pos + neg
    polarity = (pos - neg) / max(scored, 1)
    subjectivity = scored / len(tokens)
    return float(polarity), float(min(subjectivity, 1.0))
