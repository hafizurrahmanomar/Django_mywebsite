# Django_mywebsite

## 1.Install code
___

```
python -m venv myenv
myenv\Scripts\activate
pip install django
django-admin startproject mywebsite
cd mywebsite
python manage.py runserver
python manage.py startapp myapp

```
### 2. Register the App: Open the settings.py file located in the myproject directory and add your new app to the INSTALLED_APPS list:

```
INSTALLED_APPS = [
    
    'myapp.apps.MyappConfig',
]

```

```
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```