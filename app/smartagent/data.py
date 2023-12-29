
import joblib
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVR

# Load dumped objects
data_dir = Path(__file__).parent.parent.parent.joinpath('data')
model: SVR = joblib.load(data_dir.joinpath('model.pkl'))
vectorizer: TfidfVectorizer = joblib.load(data_dir.joinpath('vectorizer.pkl'))
