from django.conf.urls import url
#from gcal.views import ContactView, AboutView

from . import views


app_name = 'gcal'
urlpatterns = [
    url(r'^$', views.view_home, name='index'),
    url(r'^about/$', views.view_home, name='about'),
    url(r'^contact/$', views.view_about, name='contact'),
    url(r'^auth_user/$', views.view_google_api_user_auth, name='auth_user'),
    url(r'^callback/$', views.view_google_api_callback, name='callback'),
    url(r'^events_list/$', views.events_list, name='events_list')
]
