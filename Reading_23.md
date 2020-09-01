# Django Custom User Model

## Setup

To start, create a new Django project from the command line. We need to do several things:

create and navigate into a dedicated directory called users for our code
install Django
make a new Django project called config
make a new app users
start the local web server

`$ cd ~/Desktop`
`$ mkdir users && cd users`
`$ pipenv install django==3.0.3`
`$ pipenv shell`
`(users) $ django-admin.py startproject config .`
`(users) $ python manage.py startapp users`
`(users) $ python manage.py runserver`

## Custom User Model

Creating our initial custom user model requires four steps:

update settings.py
create a new CustomUser model
create new UserCreation and UserChangeForm
update the admin

## config/settings.py

`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig', # new
]`
...
AUTH_USER_MODEL = 'users.CustomUser' # new

Now update models.py with a new User model which we'll call CustomUser.

# users/models.py

`from django.contrib.auth.models import AbstractUser
from django.db import models`

`class CustomUser(AbstractUser):
    pass
    # add additional fields in here`

    `def __str__(self):
        return self.username`

        (users) $ touch users/forms.py
We'll update it with the following code to largely subclass the existing forms.

# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
Finally we update admin.py since the Admin is highly coupled to the default User model.

# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
And we're done! We can now run makemigrations and migrate for the first time to create a new database that uses the custom user model.

(users) $ python manage.py makemigrations users
(users) $ python manage.py migrate
Superuser
It's helpful to create a superuser that we can use to login to the admin and test out login/logout. On the command line type the following command and go through the prompts.

(users) $ python manage.py createsuperuser
Templates/Views/URLs
Our goal is a homepage with links to login, logout, and signup. Start by updating settings.py to use a project-level templates directory.

# config/settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
        ...
    },
]
Then set the redirect links for login and logout, which will both go to our home template. Add these two lines at the bottom of the file.

# config/settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
Create a new project-level templates folder and within it a registration folder as that's where Django will look for the login template.

(users) $ mkdir templates
(users) $ mkdir templates/registration
Then create four templates:

(users) $ touch templates/registration/login.html
(users) $ touch templates/base.html
(users) $ touch templates/home.html
(users) $ touch templates/signup.html
Update the files as follows:

<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
</head>
<body>
  <main>
    {% block content %}
    {% endblock %}
  </main>
</body>
</html>
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
{% if user.is_authenticated %}
  Hi {{ user.username }}!
  <p><a href="{% url 'logout' %}">logout</a></p>
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">login</a> |
  <a href="{% url 'signup' %}">signup</a>
{% endif %}
{% endblock %}
<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
{% endblock %}
<!-- templates/signup.html -->
{% extends 'base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
<h2>Sign up</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Sign up</button>
</form>
{% endblock %}
Now for our urls.py files at the project and app level.

# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
Create a urls.py file in the users app.

(users) $ touch users/urls.py
Then fill in the following code:

# users/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
Last step is our views.py file in the users app which will contain our signup form.

# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
Ok, phew! We're done. Let's test it out.

Start up the server with python manage.py runserver and go to the homepage at http://127.0.0.1:8000/.