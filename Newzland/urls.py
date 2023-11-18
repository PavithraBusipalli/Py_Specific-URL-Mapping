from Newzland.views import *
from django.urls import path,include

app_name='williamson'
urlpatterns=[
    path('william/',william,name='william'),
]

