from django.db.models.query_utils import Q
from django.db import models

from querylists.models import QueryList
from clients.models import Division, Person


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