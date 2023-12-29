from string import punctuation
from typing import Iterable

import numpy as np
from nltk import corpus, download, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import ItalianStemmer
import spacy

from models import Transaction, TRANSACTION_CATEGORIES
from smartagent.data import dictionary


nlp = spacy.load('it_core_news_sm')
stemmer = ItalianStemmer()
lang = 'italian'
try:
    stopwords = set(corpus.stopwords.words(lang))
except LookupError:
    print('stopwords not found. Downloading now...')
    download('stopwords')
    stopwords = set(corpus.stopwords.words(lang))


def load_features(transaction: Transaction) -> np.ndarray:
    if transaction.category is None or transaction.description is None:
        raise ValueError('Missing category or description')
    
    category = TRANSACTION_CATEGORIES[transaction.category]
    tokens = tokenize(f'{transaction.description} {category}')
    return np.array([tokens])


def tokenize(document: str) -> Iterable[str]:
    tokens = []
    for token in nlp(document):

    # Remove punctuation
    description = description.translate(remove_punctuation)

    # Tokenize
    words = word_tokenize(description)

    # Remove stopwords
    words = (w.lower() for w in words if not w.lower() in stopwords)

    # Lemming
    words = (lemmatizer.lemmatize(w) for w in words)

    # Stemming
    words = (stemmer.stem(w) for w in words)
    return words
