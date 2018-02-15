# Tastypie Tutorial

Project example from Django Tastypie Tutorial [(Getting Started with Tastypie)](http://django-tastypie.readthedocs.io/en/latest/tutorial.html)


## Installation

```
git clone git@github.com:werberth/tastypie-tutorial.git tastypie-tutorial
cd tastypie-tutorial
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## URLs
- **User Routes** 
	- ```/api/v1/user/```
    - ```/api/v1/user/schema/```
    - ```/api/v1/user/<pk>/```
- **Entry Routes**
    - ```/api/v1/entry/```
    - ```/api/v1/entry/schema/```
    - ```/api/v1/entry/<pk>/```
