# schedules.views
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.urls.base import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Schedule, Task
from clients.models import Person
from .forms import EditTaskForm, EditScheduleForm


def is_readonly(request, task):
    return not task.owner == request.person


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
def new_task(request):
    task = Task()
    task.name = "суть Задания"
    task.description = "более подробное описание Задания"
    task.division = request.person.division
    task.owner = request.person
    task.active = False
    task.archived = False
    return form_task(request, task)


@login_required(login_url='login')
def edit_task(request, taskid):
    task = get_object_or_404(Task.with_perms.all(request.person), pk=taskid)
    return form_task(request, task)


def form_task(request, task):
    """ Форма редактирования/просмотра Задания.

    Вызывается при создании нового и редактирования существующего Задания.
    """
    readonly = is_readonly(request, task)
    # Get Schedules of the task.
    schedules = None
    if task.id:
        schedules = Schedule.objects.filter(task=task)  # .order_by('ordernum')
    has_schedules = schedules and len(schedules) > 0

    if request.method == 'POST':
        if request.POST.get('cancel'):
            return redirect(reverse("tasks:index"))
        if request.POST.get('copy') and not task.owner == request.person:   # Чужой Опрос создаём из записи в БД
            copy_querylist = Task.objects.create(
                name='(new)' + task.name,
                description=task.description,
                division=request.person.division,
                owner=request.person,
                active=False,
                archived=False,
            )
            if has_schedules: pass
                # copy_contents(source=question, target=copy_question)
            return redirect(reverse("querylists:index"))
        form = EditTaskForm(request.POST, instance=task, readonly=readonly, contents=has_schedules)
        if form.is_valid():
            if request.POST.get('save'):
                try:
                    form.save(commit=True)
                except ValidationError as e:
                    messages.add_message(request, messages.ERROR, e.message)
                    return redirect(request.path)
            elif request.POST.get('copy'):   # Создать новый как копию текущего без сохранения изменений текущего.
                if task.owner == request.person:    # Свой вопрос создаём из формы
                    copy_task = Task.objects.create(
                        name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        division=request.person.division,
                        owner=request.person,
                        active = False,
                        archived = False,
                    )
                    if has_schedules:    pass
                        # copy_answers(source=question, target=copy_question)
            elif request.POST.get('del'):   # Удалить не связанные и архивирвоать связанные.
                if has_schedules:
                    task.archived = True
                    task.active = False
                    try:
                        task.save()
                    except ValidationError as e:
                        messages.add_message(request, messages.ERROR, e.message)
                        return redirect(request.path)
                else:
                    try:
                        task.delete()
                    except ValidationError as e:
                        messages.add_message(request, messages.ERROR, e.message)
                        return redirect(request.path)

            return redirect(reverse("querylists:index"))
    else:
        # form = EditTaskForm(instance=task, readonly=readonly, contents=has_schedules)
        form = EditTaskForm(instance=task, readonly=readonly, contents=has_schedules)

    return render(
        request,
        "edittask.html",
        {
            'task': task,
            'form': form,
            'schedulesblock': schedules_block(task, schedules),
            'readonly': readonly,
        }
    )


def schedules_block(task, schedules):
    if task.id:
        return render_to_string(
            'qcontentsblock.html',
            {
                'task': task,
                'schedules': schedules,
            }
        )
    else:
        return ''


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