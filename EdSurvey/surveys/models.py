from django.db.models.query_utils import Q
from django.db import models

from questions.models import Question, Answer, AnswerLL
from schedules.models import Attempt


class AnketaManager(models.Manager):

    @staticmethod
    def filter_expr(person):
        return Q(public=True) | (Q(owner=person) & Q(division=person.division))

    def all(self, person):
        return super().get_queryset().filter(self.filter_expr(person))

    def auth(self, user):
        res = super().get_queryset().filter(attempt__user=user)
        return res

    def get_queryset(self):
        res = super().get_queryset()
        return res


class Anketa(models.Model):
    """ Сгенерированые вопросы анкеты """
    attempt = models.ForeignKey(Attempt, on_delete=models.PROTECT)    # в ходе попытки
    question = models.ForeignKey(Question, on_delete=models.PROTECT)  # на вопрос
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    ordernum = models.PositiveIntegerField()    # Номер под которым задаётся вопрос.

    objects = AnketaManager()

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
        # unique_together = ('user', 'attempt', 'question')
        # unique_together = ('attempt', 'question')

    def __str__(self):
        return "#{}.{}".format(self.attempt, str(self.question))


class ResultManager(models.Manager):

    @staticmethod
    def filter_expr(person):
        return Q(public=True) | (Q(owner=person) & Q(division=person.division))

    def all(self, person):
        return super().get_queryset().filter(self.filter_expr(person))

    def auth(self, user):
        res = super().get_queryset().filter(anketa__attempt__user=user)
        return res

    def get_queryset(self):
        res = super().get_queryset()
        return res


class Result(models.Model):
    anketa = models.ForeignKey(Anketa, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = ResultManager()


class ResultLLManager(models.Manager):
    def auth(self, user):
        res = super().get_queryset().filter(result_ptr__anketa__attempt__user=user)
        return res

    def get_queryset(self):
        res = super().get_queryset()
        return res


class ResultLL(Result):
    result_ptr = models.OneToOneField(
        Result, on_delete=models.CASCADE,
        parent_link=True,
    )
    choice = models.ForeignKey(AnswerLL, on_delete=models.PROTECT)

    objects = ResultManager()

    def __str__(self):
        return "id{}.anketa{}.answer{}.choice{}".format(self.result_ptr.id,
                                                        self.result_ptr.anketa.id,
                                                        self.result_ptr.answer.id,
                                                        self.choice.id)
