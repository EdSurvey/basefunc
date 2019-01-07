from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^task$', views.task_index, name='task'),
    url(r'^edittask/(?P<taskid>\d+)$', views.edit_task, name='edittask'),
    url(r'^newtask$', views.new_task, name='newtask'),
    url(r'^schedule$', views.schedule_index, name='schedule'),
    # url(r'^editschedule/(?P<scheduleid>\d+)$', views.edit_schedule, name='editschedule'),
    # url(r'^addschedule/(?P<taskid>\d+)$', views.new_schedule, name='addschedule'),
]