# product-review-sentiment.py
# Late 2023 - First NLP Project: Sentiment Analysis on Product Reviews

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv('product-reviews.csv')

def get_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0.15:
        return 'Positive'
    elif analysis.sentiment.polarity < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['review_text'].apply(get_sentiment)

print("Sentiment Distribution:")
print(df['sentiment'].value_counts(normalize=True).round(3))

# Visualization
plt.figure(figsize=(8, 5))
df['sentiment'].value_counts().plot(kind='bar', color=['#4c72b0', '#55a868', '#c44e52'])
plt.title('Sentiment Analysis of Product Reviews - 2023')
plt.ylabel('Number of Reviews')
plt.tight_layout()
plt.savefig('review-sentiment-analysis.png', dpi=160)
plt.show()
