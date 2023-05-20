from textblob import TextBlob

# Funkcja sprawdzająca, czy tekst jest w języku angielskim
def is_english(text):
    blob = TextBlob(text)
    return blob.detect_language() == 'en'

# Filtracja tweetów w języku angielskim
dft['is_english'] = dft['text'].apply(is_english)
filtered_tweets = dft[dft['is_english']]