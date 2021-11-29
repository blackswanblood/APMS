from django.urls import path
from . import views
from django.conf.urls import url
from .views import index


urlpatterns =[
    url(r'^$', views.index, name = "index"),
    url(r'^insertion.html/$', views.insertion),
    url(r'^update.html/$', views.update),
    url(r'^deletion.html/$', views.deletion),
    url(r'^selection.html/$', views.selection),
    url(r'^nested_aggregation.html/$', views.nested_aggregation),
    url(r'^deletion.html/$', views.deletion),
    url(r'^join.html/$',views.join),
    url(r'^projection.html/$',views.proj),
    url(r'^agroupby.html/$', views.groupby)
]