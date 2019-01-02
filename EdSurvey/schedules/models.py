from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.db.models.query_utils import Q
from django.contrib.auth.models import User
from django.db import models

from querylists.models import QueryList
from clients.models import Division, Person, Squad


class TaskManager(models.Manager):

    @staticmethod
    def filter_expr(person):
        return Q(public=True) | (Q(owner=person) & Q(division=person.division))

    def all(self, person):
        return super().get_queryset().filter(self.filter_expr(person))


class Task(models.Model):
    """ Задачи на тестирование """
    querylist = models.ForeignKey(QueryList, on_delete=models.PROTECT)
    attempts = models.PositiveIntegerField(default=1)
    viewable = models.BooleanField(default=False)   # можно-ли просматривать свои ответы
    editable = models.BooleanField(default=False)   # можно-ли редактировать уже данные ответы
    autoclose = models.BooleanField(default=True)   # автозакрытие попытки когда есть ответы на все вопросы
    description = models.TextField()
    name = models.CharField(max_length=60)
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='владелец')
    active = models.BooleanField('активный', default=True)
    archived = models.BooleanField('архивный', default=False)

    objects = models.Manager()
    with_perms = TaskManager()

    class Meta:
        verbose_name = 'Задание на тестирование'
        verbose_name_plural = 'Задания на тестирование'

    def __str__(self):
        return "{}.{}".format(self.id, self.name)
        # return "{}({})".format(self.name, self.querylist.name)


class ScheduleManager(models.Manager):

    @staticmethod
    def filter_expr(person):
        return Q(owner=person)

    def all(self, person):
        return super().get_queryset().filter(self.filter_expr(person))


class Schedule(models.Model):
    """ Расписание задач """
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='владелец')
    # squads = models.ManyToManyField(Squad, blank=True, verbose_name='назначение')

    objects = models.Manager()
    with_perms = ScheduleManager()

    class Meta:
        verbose_name = 'Назначеное тестирование'
        verbose_name_plural = 'Расписание заданий'

    def __str__(self):
        return "{} {}".format(self.task.name, self.name)


class AttemptManager(models.Manager):

    @staticmethod
    def filter_expr(person):
        return Q(public=True) | (Q(owner=person) & Q(division=person.division))

    def all(self, person):
        return super().get_queryset().filter(self.filter_expr(person))


class Attempt(models.Model):
    """ Попытки сдать тест-кейс """
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    started = models.DateTimeField(auto_now_add=True, auto_now=False)
    finished = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)

    objects = models.Manager()
    with_perms = AttemptManager()

    class Meta:
        verbose_name = 'Попытка пройти тест'
        verbose_name_plural = 'Попытки пройти тест'

    def __str__(self):
        return "#{}.{}".format(str(self.started), str(self.schedule))


def schedule_pre_save(instance, **kwargs):
    """ Validation
    - Нельзя менять расписание, если по нему уже есть начатые попытки.
    """
    if Schedule.objects.all().filter(pk=instance.id).count() > 0:
        if Attempt.objects.all().filter(schedule=instance).count() > 0:
            raise ValidationError("Нельзя изменять расписание, если по нему уже есть начатые попытки.")


pre_save.connect(schedule_pre_save, sender=Schedule)


# Cross-Models Validations

def task_pre_save(instance, **kwargs):
    """ Validation
    - Нельзя изменять Задание, если по нему уже существует расписание.
    """
    if Task.objects.all().filter(pk=instance.id).count() > 0:
        if Schedule.objects.all().filter(task=instance).count() > 0:
            raise ValidationError("Нельзя изменять задание, если по нему уже существует расписание.")


pre_save.connect(task_pre_save, sender=Task)


def attempt_pre_save(instance, **kwargs):
    try:
        # opened_attempt =
        Attempt.objects.get(
            schedule=instance.schedule,
            finished__isnull=True,
            user=instance.user,
        )
    except ObjectDoesNotExist:
        # Открытых попыток нет.
        return
    try:
        # считываем предыдущее состояние
        attempt = Attempt.objects.get(pk=instance.id)
    except ObjectDoesNotExist:
        # Создаётся новая попытка, но есть opened_attempt
        raise ValidationError("Нельзя начать новую попытку пока существует незавершённая.")

    # Проверяем на внесение изменений
    if attempt.finished:
        raise ValidationError("Нельзя вносить изменения в завершённую попытку.")
    elif instance.started > instance.finished:
        raise ValidationError("Дата завершения должна быть позже даты начала.")


pre_save.connect(attempt_pre_save, sender=Attempt)
