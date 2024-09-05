import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure the VADER lexicon is downloaded
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Create a SentimentIntensityAnalyzer object.
    sid = SentimentIntensityAnalyzer()
    
    # Get the polarity scores for the text.
    sentiment_scores = sid.polarity_scores(text)
    
    # Determine sentiment based on compound score.
    if sentiment_scores['compound'] >= 0.05:
        return 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'
