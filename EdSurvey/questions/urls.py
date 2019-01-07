# questions.urls
# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^answersbyquestion/(?P<questionid>\d+)$', views.answers_by_question, name='answersbyquestion'),
    url(r'^editquestion/(?P<questionid>\d+)$', views.edit_question, name='editquestion'),
    url(r'^newquestion$', views.new_question, name='newquestion'),
    url(r'^editanswer/(?P<answerid>\d+)$', views.edit_answer, name='editanswer'),
    url(r'^newanswer/(?P<questionid>\d+)$', views.new_answer, name='newanswer'),
    # API using DRF
    # path('api/', views.ApiView.as_view(), name='api'),
    url(r'^api/', views.ApiView.as_view(), name='api'),
    url(r'^list/', views.QuestionView.as_view(), name='question-list'),
]