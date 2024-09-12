# What is Django?
#### Python-based web framework used for rapid development of web applications.

# Install Django
```
pip install django
```

## Creating a project
```
django-admin startproject projectname
```

# Starting a server
```
python manage.py runserver
```

# Create Django App
```
python manage.py startapp appname
```
## After Create Django App

```js
INSTALLED_APPS = [
    appName // add in Project setting file
    ....
]
```
# Setup Template and static Folder
### All Change in setting file
## Template
```js
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], // Add this Line 57 on setting
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## Static
```js
import os
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

# Modal (Database Table)
## Add in app modal file
```js
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    date = models.DateField()
    
    def __str__(self):
        return self.name
```
## Add in app admin file
```
from appName.models import Contact
admin.site.register(Contact)
```
## Run This Command
```
python manage.py makemigrations
python manage.py migrate
```

#  deploy a App

## Add this line in Project urls file
```
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
```

add in requirements.txt
```
gunicorn==23.0.0
```
## Start Command
```
gunicorn projectName.wsgi
```