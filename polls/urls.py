from django.conf.urls import patterns, include, url
from django.views import *
from polls.views import *
 
urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^(?P<poll_id>\d+)/$', detail),
    url(r'^(?P<poll_id>\d+)/results/$', results),
    url(r'^(?P<poll_id>\d+)/vote/$', vote),
)