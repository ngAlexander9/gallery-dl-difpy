# gallery-dl-difpy

combines gallery-dl to difpy to download media links from url list, then delete duplicate images

## gallery-dl CLI vs library

gallery-dl is designed to be used from the command line - it is possible to import as a library but documentation on usage is poor. For the time being, the CLI method will be used for gallery-dl

## setup

1st time setup

- `python -m venv venv` create virtualenv
- `.\venv\Scripts\activate.ps1` start venv
- `pip freeze > requirements.txt` freeze dependencies
- `pip install -r requirements.txt` install dependencies
- `deactivate` deactivate venv

## usage

- activate
- python main
