# Empowering Precision Medicine: The Neurodegenerative Diseases and Cancer Biobank

## _Powered by: BiHELab, Ionian University_

### Admin settings:

- create .env according to .env_template

- create virtual environment and run the project

for windows:

```<bash>

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000

```

for linux:

```<bash>

python -m venv venv

venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000

```
