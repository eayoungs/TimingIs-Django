from django.conf.urls import url
#from gcal.views import ContactView, AboutView

from . import views


app_name = 'gcal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about_view, name='about'),
    url(r'^contact/$', views.contact_view, name='contact'),
    url(r'^auth_user/$', views.auth_user, name='auth_user'),
    url(r'^callback/$', views.callback, name='callback'),
    url(r'^events_list/$', views.events_list, name='events_list')
]
