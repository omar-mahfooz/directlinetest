step 0 

setup environemnt , have pip installed , have python installed min 3.6

pip install django-rest

this will install django too 

step1:
create a  project
e.g 
django-admin startproject technicaltest

step2:
navigate to directory, e.g cd technicaltest to find python manage.py which we will use.

step 3:
create an application
manage.py startapp [app_name]  

e.g 

manage.py startapp total


step4: 
register the new app , in the technicaltest/settings.py
e.g

INSTALLED_APPS = [
    'total',
    ... # Leave all the other INSTALLED_APPS
]

step5 :
create db file, in this case using sqlite as prebuilt , 

python manage.py makemigrations
python manage.py migrate

step6:

create super user for admin / testing

python manage.py createsuperuser


step7:

test admin site with your chosen creds,

python manage.py runserver
defaul port chosen, 8000, go to  127.0.0.1/8000


step8
create a model in total/models.py

from django.db import models
# Create your models here.



class Total(models.Model):
    numbers_to_add = list(range(10000001))

    total = models.IntegerField()

    def __unicode__(self):
        return "Total: %s" %self.total


this class takes models.Model as a parameter which is a standard model parameter.
create a total field class attrib , using the Interfield, CharField may also be used for more
complex situations e.g arrays, but it needs to be formatted to be abled to do cals, e.g converted.


def function returns the values of the object to the server.


step9:

update your new changes by migrating . 
python manage.py makemigrations

step10: 

register your new class , so you can manage it with the admin panel, or if you can connect to the DB directly
for this pycharm ultimate is required...

from django.contrib import admin
from .models import Total
# Register your models here.
admin.site.register(Total)


step11:

upload data using admin panel, or manually push data to the server using push function in webserver.(not available at this point)

python manage.py runserver 

loging to admin site, my going to : localhost:8000/admin

create your chosen entry.

step 12:

go to settings.py 

add rest_framework

INSTALLED_APPS = [
    # All your installed apps stay the same
    ...
    'rest_framework',
]



step 13: 

seriliaze your data , for compatibility with Json

from rest_framework import serializers
from .models import Total
from rest_framework.serializers import ModelSerializer


class TotalSerializer(serializers.ModelSerializer):


    class Meta:
        model = Total
        fields = ('total',)
		
		
step14:

create a view

from django.shortcuts import render, HttpResponse

from .models import Total
from rest_framework import viewsets
from .serializers import TotalSerializer

# Create your views here.

class TotalViewSet(viewsets.ModelViewSet):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer
    model = Total


step15:

routing , create site URLS and API URls for management

go to technicaltest/urls.py 

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('total.urls')),
]


add total.urls 

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'total', views.TotalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


step16:

Final test 

 go to localhost:8000 


