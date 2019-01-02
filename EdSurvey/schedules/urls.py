from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^schedule$', views.schedule_index, name='schedule'),
    url(r'^task$', views.task_index, name='task'),
    # url(r'^schedule/(?P<scheduleid>\d+)$', views.schedule_info, name='scheduleinfo'),
]