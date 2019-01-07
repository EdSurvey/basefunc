from datetime import timedelta

from django.utils.timezone import now

from ..querylists import install
from ..querylists.install import querylist1, querylist2
from ..clients.install import \
    division_the_site, division_the_site_common, \
    site1_user

from schedules.models import Task, Schedule


def add_schedule(task, start, finish, name, description, owner):
    print("Adding schedule: task={}, name={} ".format(task, name))
    schedule = Schedule(
        task=task,
        start=start,
        finish=finish,
        name=name,
        description=description,
        owner=owner,
    )
    schedule.save()
    return schedule

task1 = Task.objects.create(
    querylist=querylist1,
    attempts=1,
    viewable=False,
    editable=False,
    autoclose=True,
    description="""NoEdit NoView Auto""",
    name="Для отладки расписаний",
    division=division_the_site,
    public=True,
    owner=site1_user,
)
task1_sched1 = add_schedule(
    task=task1,
    start=now(),
    finish=now() + timedelta(hours=1),
    name="на 1 час",
    description="""доступен в течении 1 часа""",
    owner=site1_user,
)
task1_sched2 = add_schedule(
    task=task1,
    start=now(),
    finish=now() + timedelta(days=1),
    name="на 1 день",
    description="""доступен в течении суток""",
    owner=site1_user,
)
# task1_sched3 = add_schedule(
#     task=task1,
#     start=now(),
#     finish=now() + timedelta(days=1),
#     name="до конца дня",
#     description="""доступен до полуночи""",
# )
task1_sched4 = add_schedule(
    task=task1,
    start=now(),
    finish=now() + timedelta(days=31),
    name="на 1 месяц",
    description="""доступен в течении месяца""",
    owner=site1_user,
)