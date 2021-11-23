from django.urls import path
from . import views
from django.conf.urls import url
from .views import index


urlpatterns =[
    url(r'^$', views.index, name = "index"),
    url(r'^insertion.html/$', views.insertion),
    url(r'^update.html/$', views.update)
]