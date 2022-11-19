# django-training

a music platform on which artists can sign up and put up their albums for sale



## Installation

install Python 

```bash
  For windows - Download latest version from the official website: 
        https://www.python.org/downloads/
```
    
## Run Locally

Clone django-training

```bash
  git clone https://github.com/3RB16/django-training.git
```

Go to the project directory

```bash
  cd django-training
```
install Virtual Enviorentment

```bash
  python -m venv env
```

Acitve Virtual Enviorentment

```bash
  env/Scripts/activate
```

Install poetry

```bash
  python -m pip install poetry
```

Install dependencies

```bash
  poetry install
```

Start the server

```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
```
