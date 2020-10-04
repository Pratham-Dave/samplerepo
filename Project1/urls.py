from django.urls import path
# from django.conf.urls.defaults import *
from . import views

urlpatterns = [
    path('', views.index, name="index")
]
# urlpatterns += patterns('', (r'', include('gmapi.urls.media')))