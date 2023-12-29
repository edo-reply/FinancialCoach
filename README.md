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
Firstly run this command to generate the model based on the training dataset
```sh
python -m train
```

To run the webserver execute these commands inside the root directory:
```sh
source venv/Scripts/activate
python app/app.py
```
