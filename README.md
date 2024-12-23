# lun_ua

A simplified version of lun.ua 

![Tests](https://github.com/nikita88575/lun_ua/actions/workflows/ci.yml/badge.svg)

## Technologies

* Python
* Django
* Materialize
* PostgreSQL
* Github Actions

## Linux

1. Create virtual environment  
   `python -m venv venv`
1. Activate virtual environment  
   `source venv/bin/activate`
1. Install dependencies  
   `pip install -r requirements.txt`
1. Setup environment variables  
   `cp .env.example .env`
1. Run migrations  
   `python3 manage.py migrate`
1. Run server
   `python3 manage.py runserver`
1. Open in browser http://localhost:8000
1. Create superuser for access to admin panel http://localhost:8000/admin  
   `python manage.py createsuperuser`

## Before commit

Autoformat code  
`make autofmt`  
Check code  
`make lint`   
Run tests  
`make test`

## Internalization

1. Install gettext on Linux

   `sudo apt install gettext`

   Install gettext om MacOS

   `brew install gettext`
2. Make messages

   `python manage.py makemessages -l uk --ignore=venv`
3. Compile messages  

   `python manage.py compilemessages -l uk --ignore=venv`

## Front-End
1. Install sass https://sass-lang.com/install/
2. Add filewatcher in IDE for compile sass to css
3. Don't change css files directly, they will be rewritten, change scss files

## License

[MIT](https://choosealicense.com/licenses/mit/)

