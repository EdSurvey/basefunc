# schedules.views
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Schedule, Task
from clients.models import Person


@login_required(login_url='login')
def task_index(request):
    person = Person.objects.get(pk=request.session['person_id'])
    tasks = Task.with_perms.all(person).order_by('id')
    return render(
        request,
        'tasks.html',
        {
            'tasks': tasks,
        }
    )


@login_required(login_url='login')
def schedule_index(request):
    person = Person.objects.get(pk=request.session['person_id'])
    opened_schedules = Schedule.with_perms.all(person).filter(start__lt=now(), finish__gt=now()).order_by('task__id', '-start', 'name')
    closed_schedules = Schedule.with_perms.all(person).filter(finish__lt=now()).order_by('task__id', '-start', '-finish', 'name')
    return render(
        request,
        'schedules.html',
        {
            'opened': opened_schedules,
            'closed': closed_schedules,
        }
    )