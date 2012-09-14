from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to
from django.conf import settings

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='whistlepig.home'),
)