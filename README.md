# Financial Coach

## Installation
Run the following commands inside the root directory:
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python -m spacy download it_core_news_sm
```

## Usage
When you want to retrain the model after a change in the dataset run this command to generate it
```sh
source venv/Scripts/activate
python app/train.py
```

To run the webserver execute these commands inside the root directory:
```sh
source venv/Scripts/activate
python app/app.py
```
