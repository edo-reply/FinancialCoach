from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, precision_score

from smartagent.preprocess import tokenize

if __name__ == '__main__':
    data_dir = Path(__file__).parent.parent.joinpath('data')

    ds = pd.read_csv(data_dir.joinpath('dataset.csv'))

    vectorizer = TfidfVectorizer(tokenizer=tokenize, token_pattern=None, lowercase=True) # type: ignore

    train_ds, test_ds = train_test_split(ds, test_size=.2)


    transaction_descriptor = train_ds['transaction_description'] + ' ' + train_ds['transaction_category']
    vectorizer.fit(transaction_descriptor)

    features = vectorizer.transform(transaction_descriptor)

    print('descriptions shape:', transaction_descriptor.shape)
    print('features shape:', features.shape)

    model = SVR(verbose=True)

    model.fit(X=features, y=train_ds['transaction_score'])

    joblib.dump(vectorizer, data_dir.joinpath('vectorizer.pkl'))
    joblib.dump(model, data_dir.joinpath('model.pkl'))

    # Valuta le prestazioni del modello
    X_test = vectorizer.transform(test_ds['transaction_description'] + ' ' + test_ds['transaction_category'])
    y_test = test_ds['transaction_score'].to_numpy()
    predictions = model.predict(X_test)


    print(y_test.shape, predictions.shape)
    mse = mean_squared_error(y_test, predictions)
    # accuracy = accuracy_score(y_test, predictions)
    # accuracy_round = accuracy_score(np.rint(y_test).astype(int), np.rint(predictions).astype(int))
    precision_round = precision_score(np.rint(y_test).astype(int), np.rint(predictions).astype(int), average='weighted')
    # report = classification_report(y_test, predictions)

    print('mse', mse)
    # print('accuracy', accuracy)
    # print('accuracy_round', accuracy_round)
    print('precision_round', precision_round)
    # print('report', report)

    test_ds['calculated_score'] = predictions
    test_ds['calculated_score_round'] = np.rint(predictions).astype(int)
    test_ds[['transaction_description', 'transaction_category', 'transaction_score', 'calculated_score_round', 'calculated_score']].to_csv('test.csv')
