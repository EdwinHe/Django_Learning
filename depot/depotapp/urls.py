from django.conf.urls import patterns, include, url
from depotapp import views

urlpatterns = patterns('',
    url(r'^$', views.depotapp_test, name = 'depotapp'),
)
