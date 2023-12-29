from string import punctuation
from typing import Iterable

import nltk
from nltk.stem.snowball import ItalianStemmer
import spacy


nlp = spacy.load('it_core_news_sm')
stemmer = ItalianStemmer()
lang = 'italian'
try:
    stopwords = set(nltk.corpus.stopwords.words(lang))
except LookupError:
    print('stopwords not found. Downloading now...')
    nltk.download('stopwords')
    stopwords = set(nltk.corpus.stopwords.words(lang))

def tokenize(document: str) -> Iterable[str]:
    tokens = []
    for token in nlp(document):
        if token.text not in punctuation and token.text not in stopwords:
            lemma = token.lemma_
            stem = stemmer.stem(lemma)
            tokens.append(stem)
    return tokens
