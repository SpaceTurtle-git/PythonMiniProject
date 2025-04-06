py -3 -m venv .venv

.venv\scripts\activate
py manage.py makemigrations
py manage.py migrate

select interpreter command pallete
python -m pip install --upgrade pip
python -m pip install django
django-admin startproject netflix .
python manage.py migrate
py manage.py runserver

tutorial 1 :
in setting.py
import os 
'DIRS': [os.path.join(BASE_DIR, "templates")],
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = '/media/'
MEDFIA_ROOT = os.path.join(BASE_DIR, "media")
#LOGIN_REDIRECT_URL = ""
#LOGIN_URL = "login"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "miniapp",
]
stuff between 
{% block content %}   
{% endblock content %}
gets displayed

pip install pillow
pip show pillow

(.venv) PS C:\Users\rockf\OneDrive\Documents\PythonMiniProject> python manage.py createsuperuser
Username: turtle
Email address: turtle@sfit.com
Password: 
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(.venv) PS C:\Users\rockf\OneDrive\Documents\PythonMiniProject> 
