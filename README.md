# django-training

a music platform on which artists can sign up and put up their albums for sale



## Installation

install Python 

```bash
  For windows - Download latest version from the official website: 
    https://www.python.org/downloads/

  For Centos - use yum:
    sudo yum install python3

  For Ubuntu - use apt-get:
    sudo apt install python3

```

Install poetry

```bash
  python -m pip install poetry
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

Acitve Virtual Enviorentment

```bash
  env/Scripts/acitve
```

Install dependencies

```bash
  poetry Install
```

Start the server

```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
```
