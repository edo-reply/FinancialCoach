import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def preprocess(self, descriptions):
       # Tokenize
       stopwords = set(nltk.corpus.stopwords.words('english'))
       trans = str.maketrans('', '', string.punctuation)
       filtered_sentences = []
       for d in descriptions:
           tokens = nltk.word_tokenize(d.translate(trans))
           filtered_sentences.append([w.lower() for w in tokens if not w.lower() in stopwords])

       # Lemming
       filtered_sentences_lem = [[self.lemmatizer.lemmatize(w) for w in s] for s in filtered_sentences]

       # Stemming
       filtered_sentences_lem_stem = [[self.stemmer.stem(w) for w in s] for s in filtered_sentences_lem]
       return filtered_sentences_lem_stem
