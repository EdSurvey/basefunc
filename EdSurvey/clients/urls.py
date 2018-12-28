from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^aka$', views.aka, name='aka'),
]
