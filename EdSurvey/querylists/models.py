from django.db.models.query_utils import Q
from django.db import models

from questions.models import Question
from clients.models import Division, Person

#   querylists.models


class QuerylistManager(models.Manager):

    @staticmethod
    def filter_expr(person):
        return Q(public=True) | (Q(owner=person) & Q(division=person.division))

    def all(self, person):
        return super().get_queryset().filter(self.filter_expr(person))


class QueryList(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='владелец')
    active = models.BooleanField('активный', default=True)
    archived = models.BooleanField('архивный', default=False)

    objects = models.Manager()
    with_perms = QuerylistManager()

    class Meta:
        verbose_name = 'Опросник'
        verbose_name_plural = 'Опросники'

    def __str__(self):
        return "{}.{}".format(self.id, self.name)


class QueryContent(models.Model):
    querylist = models.ForeignKey(QueryList, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    ordernum = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Наполнение опросника'
        verbose_name_plural = 'Наполнение опросников'
        unique_together = ('querylist', 'question')

    def check_perm(self, person):
        return QueryList.with_perms.all(person).filter(pk=self.querylist.id)[:1].count() == 1

    def __str__(self):
        return "{}-{}".format(self.querylist, self.question)
