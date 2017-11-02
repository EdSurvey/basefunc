from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^editquerylist/(?P<questionid>\d+)$', views.edit_querylist, name='editquerylist'),
    # url(r'^newquerylist$', views.new_querylist, name='newquerylist'),
    # url(r'^editqcontents/(?P<qlistid>\d+)$', views.edit_qcontents, name='editqcontents'),
    # url(r'^addqcontent/(?P<qlistid>\d+)$', views.new_qcontent, name='addqcontent'),
]