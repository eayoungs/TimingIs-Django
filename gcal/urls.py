from django.conf.urls import url

from . import views


app_name = 'gcal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events_list/$', views.events_list, name='events_list')
]
