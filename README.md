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

# python manage.py django command list

- startproject: Creates a new Django project.
```
django-admin startproject projectname
```
- startapp: Creates a new Django app within a project.
```
python manage.py startapp appname
```
- runserver: Starts the development server.
```
python manage.py runserver
```
- shell: Opens the Python shell with Django environment loaded.
```
python manage.py shell

```
- makemigrations: Generates new database migration files based on model changes.
```
python manage.py makemigrations
```
- migrate: Applies database migrations to synchronize the database schema.
```
python manage.py migrate
```
- createsuperuser: Creates a superuser for the Django admin.
```
python manage.py createsuperuser
```
- collectstatic: Gathers static files from your apps into a single directory.
```
python manage.py collectstatic
```
- test: Runs tests for your Django project.
```
python manage.py test
```
- dbshell: Opens a command-line interface to the database.

```
python manage.py dbshell
```
- check: Checks for issues in your project without making migrations or touching the database.
```
python manage.py check
```
- showmigrations: Displays a list of all migrations and their status.
```
python manage.py showmigrations
```
- shell_plus: Enhanced version of the shell with additional features (requires django-extensions).
```
python manage.py shell_plus
```
- dumpdata: Outputs the contents of the database as a JSON or XML fixture.
```
python manage.py dumpdata
```
- loaddata: Loads data from a fixture into the database.
```
python manage.py loaddata
```
- flush: Resets the database by removing all data.
```
python manage.py flush
```
- createsuperuser: Creates a superuser for the Django admin.

```
python manage.py createsuperuser
``
- startapp: Creates a new app within a Django project.
```
python manage.py startapp appname
```
- runserver: Starts the development server.
```
python manage.py runserver
```
- runscript: Runs a Python script in the context of a Django project (requires django-extensions).
```
python manage.py runscript script_name
```
- graph_models: Creates a visual representation of your Django models (requires django-extensions).
```
python manage.py graph_models -a > models.dot
```
- dbshell: Opens a command-line interface to the database.
```
python manage.py dbshell
```
- shell_plus: Enhanced version of the shell with additional features (requires django-extensions).
```
python manage.py shell_plus
```
- test: Runs tests for your Django project.
```
python manage.py test
```
- check: Checks for issues in your project without making migrations or touching the database.
```
python manage.py check
```
- check — deploy: Checks for common issues in a deployment-ready project.
```
python manage.py check --deploy
```
- show_urls: Displays all URLs defined in the project.
```
python manage.py show_urls
```