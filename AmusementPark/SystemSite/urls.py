from django.urls import path
from . import views
from django.conf.urls import url
from .views import index


urlpatterns =[
    url(r'^$', views.index, name = "index"),
    # url(r'^viewalltourists/$', views.viewAllTourists),
]