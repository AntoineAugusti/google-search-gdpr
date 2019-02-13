# Google Search GDPR

## What's this?
Generate a CSV file of your Google Search queries from your Google Takeout export.

## Installation
```sh
git clone git@github.com:AntoineAugusti/google-search-gdpr.git
cd google-search-gdpr
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
$ python main.py -h
usage: main.py [-h] filepath

positional arguments:
  filepath    The full path to the Google Search JSON file

optional arguments:
  -h, --help  show this help message and exit
```

Therefore, you can call the script like this: `python main.py searches.json`

## Generated CSV
See the file [data_sample.csv](data_sample.csv) to look at a sample file!
