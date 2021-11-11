from django.urls import path

from . import views

from django.conf.urls import url
from .views import index


urlpatterns =[
    url(r'^$', index, name = "index"),
]