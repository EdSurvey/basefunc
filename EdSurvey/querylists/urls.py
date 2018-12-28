from django.conf.urls import url

from . import views

#   querylists.urls

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^editquerylist/(?P<querylistid>\d+)$', views.edit_querylist, name='editquerylist'),
    url(r'^newquerylist$', views.new_querylist, name='newquerylist'),
    url(r'^editqcontents/(?P<qcontentid>\d+)$', views.edit_qcontent, name='editqcontent'),
    url(r'^addqcontent/(?P<qlistid>\d+)$', views.new_qcontent, name='addqcontent'),
]