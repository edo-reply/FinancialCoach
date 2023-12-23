from string import punctuation
from typing import Generator

import numpy as np
from nltk import corpus, download, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from models import Transaction
from smartagent.data import dictionary


lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
remove_punctuation = str.maketrans('', '', punctuation)
lang = 'english'
try:
    stopwords = set(corpus.stopwords.words(lang))
except LookupError:
    print('stopwords not found. Downloading now...')
    download('stopwords')
    stopwords = set(corpus.stopwords.words(lang))


def load_features(transaction: Transaction) -> np.ndarray:
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
