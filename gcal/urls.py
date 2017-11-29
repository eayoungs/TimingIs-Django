from django.conf.urls import url
from gcal.views import ContactView, AboutView

from . import views


app_name = 'gcal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^events_list/$', views.events_list, name='events_list')
]
