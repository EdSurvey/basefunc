from django.conf.urls import url, include

from . import views

#   home.urls


urlpatterns = [
    url(r'^$', views.index),
]