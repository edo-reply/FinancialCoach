from pathlib import Path

from numpy import ndarray
from sklearn.svm import SVR
import joblib


# Load dumped files
data_dir = Path(__file__).parent.joinpath('data')
model: SVR = joblib.load(data_dir.joinpath('model.pkl'))
dictionary: ndarray = joblib.load(data_dir.joinpath('dictionary.pkl'))
