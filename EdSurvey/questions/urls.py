from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^answersbyquestion/(?P<questionid>\d+)$', views.answers_by_question, name='answersbyquestion'),
    url(r'^editquestion/(?P<questionid>\d+)$', views.edit_question, name='editquestion'),
    url(r'^newquestion$', views.new_question, name='newquestion'),
]