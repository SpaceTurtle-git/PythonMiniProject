py -3 -m venv .venv
.venv\scripts\activate
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