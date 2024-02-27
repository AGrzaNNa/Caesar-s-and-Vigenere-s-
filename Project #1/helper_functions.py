# Download English words corpus from NLTK
import nltk

nltk.download('words')
english_words = set(nltk.corpus.words.words())

# Check of eng existence of particular word
def validate_word(word):
    return word.lower() in english_words

