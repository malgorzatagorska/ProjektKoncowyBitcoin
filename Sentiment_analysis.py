from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Przykładowe użycie funkcji analyze_sentiment()
tweet_text = "I love this product! It's amazing!"
sentiment_score = analyze_sentiment(tweet_text)
print("Sentiment Score:", sentiment_score)

# Określenie zakresu dat
filtered_tweets = filtered_tweets[(filtered_tweets['timestamp'] >= startdate) & (filtered_tweets['timestamp'] <= enddate)]

# Analiza sentymentu dla tweetów
filtered_tweets['sentiment'] = filtered_tweets['text'].apply(analyze_sentiment)

# Wyświetlenie przefiltrowanych tweetów z wynikiem sentymentu
print(filtered_tweets[['text', 'sentiment']])