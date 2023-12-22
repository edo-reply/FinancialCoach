import string
from typing import Generator
import numpy as np
from nltk import word_tokenize, corpus
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from models import Transaction

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stopwords = set(corpus.stopwords.words('english'))
remove_punctuation = str.maketrans('', '', string.punctuation)


def load_features(transaction: Transaction, dictionary) -> np.ndarray:
    if transaction.description is not None:
        description_tokens = tokenize_description(transaction.description)
    # result = description IDF + category IDF
    return np.array([])


def tokenize_description(description: str) -> Generator[str, None, None]:
    # Remove punctuation
    description = description.translate(remove_punctuation)

    # Tokenize
    tokens = word_tokenize(description)

    # Remove stopwords
    words = (w.lower() for w in tokens if not w.lower() in stopwords)

    # Lemming
    words = (lemmatizer.lemmatize(w) for w in words)

    # Stemming
    words = (stemmer.stem(w) for w in words)
    return words
