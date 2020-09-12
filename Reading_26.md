# Django Rest Framework Permissions

Permissions in Django Rest Framework are used to grant or deny access for different types of users to different parts of the API. Permissions are very useful when serving API resources/end-points with certain restrictions.

## Permissions Flow in DRF¶
Whenever any request comes to DRF then it enters the "dispatch" method. "dispatch" method should route the request to appropriate request method like "get", "post", "put", "delete", etc. But, before routing the request to the one of these methods it will checks the authentication, "permissions" and then it checks throttles(i.e used to limit the number of requests per user or per IP). In Django REST framework we always define permissions as a list. In DRF we can setup global permission classes or we can specify the permission classes in Views and Viewsets. If all permission checks are valid then request will be passed to appropriate method (i.e "get", "post", "put", "delete", etc. ) based on the request type otherwise an exception will be raised.

The exception can be one of exceptions.PermissionDenied or exceptions.NotAuthenticated . If authentication fails then it returns status code of 401 and if any other permissions fails then it will return the status code of 403.

## Default Permissions Classes provided by DRF¶

Django rest framework provides the following permission classes which are used frequently..

## AllowAny¶

This permission class do not restrict the user to access the API resource.
IsAuthenticated¶
This permission class only permits authenticated or logged in users to access the API resource.

## IsAdminUser¶

This permission class only allows Django Admin Users(i.e user.is_staff = True) to access the api resource and all other users will not be able access the API resource.
IsAuthenticatedOrReadOnly¶
This permission class allows authenticated users to perform read and write operations on the API resource.
All users which are not authenticated will have read access only. If they try to update the API resource then it will raise permission denied error.
DjangoModelPermissions¶
It is based on model permissions provided by django.contrib.auth.
It only be applied to views that have a queryset property.
It only applied on authenticated users who has the relevant model permissions assigned.

POST requests require the user to have the add permission on the model.
PUT and PATCH requests require the user to have the change permission on the model.
DELETE requests require the user to have the delete permission on the model.
DjangoModelPermissionsOrAnonReadOnly¶
Same as DjangoModelPermissions, but it also allows unauthenticated users to have read-only access to the API resource.

Configuring the Permissions Gobally in "settings.py"¶
If we configure the global permission then these permission will apply on all API Views and ViewSets unless these permissions are overidden in Views and ViewSets. Let's see how to configure the permission globally.


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
DEFAULT_PERMISSION_CLASSES takes data type of list or tuple or any iterable types. We can configure multiple permissions globally.

Working with Permissions in DRF¶
In the last article we have seen how to setup thetoken based authentication in Django REST Framework. Let's write some code to know how to work with permissions.

urls.py


from . import views
urlpatterns = [
    path('api/protected/', views.ProtectedAPIView.as_view(), name='protected'),
]
views.py


from rest_framework.response import Response
from rest_framework.views import APIView

class ProtectedAPIView(APIView):

    def get(self, request, format=None):
        content = {
            'message': 'Hey! you have authenticated!'
        }
        return Response(content)
We have written api view now it's time to test the above API endpoint (i.e "api/protected/"). Let's do this using python requests.


import requests
headers = {"Authorization": "Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b", "content-type": "application/json"}
r = requests.get("https://localhost:8000/api/protected/", headers=headers)
print(r.json())
# Output: {"message": "Hey! you have authenticated!"}
In above code we have not defined the any permission class but it will ask for user authentication permission to access the API resource. Because we have defined the authentication permission globally. So, we have passed the authentication token in the python request to access the API resource.

Writing Custom Permissions in DRF¶
In Django REST Framework we can use custom permission classes also. We can write two types of permission classes "view level" and "object level" .

View level permissions

We use these permission when we want to check the user permission/access level before passing the request to process it further.
Object level permissions

We use it when we want to check the user permission on object level. For example, let's consider the book writer scenario where user writes books and if only allow its owner to modify it. In that kind of scenarios we use object level permissions.
Let's write a custom permission to block some IP address to access the API.

permissions.py


from rest_framework import permissions
from .models import Blacklist

class BlacklistPermission(permissions.BasePermission):
    """
    Permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted
"BasePermission" is the base class for all custom permissions. It provides the method "has_permission" to implement our custom permissions. In above code we have overriden "has_permission" method to implement our permission functionality. It's an example for view level permission.

Let's write some code to implement object level permission.

models.py


from django.db import models
from .models import User

class Book(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Blacklist(models.Model):
    ip_addr = models.GenericIPAddressField()
permissions.py


from rest_framework import permissions
from .models import Blacklist, Writer

class IsBookOwner(permissions.BasePermission):
    """
    Check if user is Book owner or not.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
urls.py


from . import views
urlpatterns = [
    path('api/book/<int:pk>/', views.ProtectedAPIView.as_view(), name='protected'),
]
serializers.py


from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSeriaizer):
    class Meta:
        model = Book
views.py


from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import RetrieveAPIView
from .permissions import IsBookOwner, BlacklistPermission
from .serializers import BookSerializer

class BookAPIView(RetrieveAPIView):
    permission_classes = [BlacklistPermission, IsAuthenticated, IsBookOwner]
    serializer_class = BookSerializer
We have written api view now it's time to test the above API endpoint (i.e "api/protected/"). Let's do this using python requests.


import requests
headers = {"Authorization": "Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b", "content-type": "application/json"}
r = requests.get("https://localhost:8000/api/book/1/", headers=headers)
print(r.json())
# Output: {"title": "Smart People Do Smart Things!"}#