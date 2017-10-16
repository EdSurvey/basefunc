from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

from clients.models import Division, Person


RADIOBUTTON = 'RB'  # (*) One -from- List
CHECKBOX = 'CB'  # [v] Some -from- List
LINKEDLISTS = 'LL'  # Link One from first list -to- One from other list
QUESTION_TYPE_CHOICES = (
    (RADIOBUTTON, 'Один из ...'),
    (CHECKBOX, 'Несколько из ...'),
    (LINKEDLISTS, "Путанка"),
)

class QuestionManager(models.Manager):
    def all(self, person):
        qset = Q(public=True) | (Q(owner=person) & Q(division=person.division))
        return super().get_queryset().filter(qset)


class Question(models.Model):
    name = models.CharField('наименование', max_length=60)
    description = models.TextField('полное описание')
    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name='организация')
    public = models.BooleanField('публичное', default=False)
    qtype = models.CharField(max_length=2,
                             choices=QUESTION_TYPE_CHOICES,
                             default=RADIOBUTTON,
                             verbose_name='Тип вопроса',)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='личность-владелец')
    active = models.BooleanField('активно', default=True)

    objects = models.Manager()
    with_perms = QuestionManager()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return "{}.{}.{}".format(self.id, self.qtype, self.name)


def question_pre_save(instance, **kwargs):
    # Проверка на изменение типа вопроса (qtype)
    # select 1 from Answer where Answer.question = self.id limit 1
    cntRB = AnswerRB.objects.all().filter(question=instance)[:1].count()
    cntCB = AnswerCB.objects.all().filter(question=instance)[:1].count()
    cntLL = AnswerLL.objects.all().filter(question=instance)[:1].count()
    if instance.qtype not in [qtype for qtype,txt in QUESTION_TYPE_CHOICES]:
        raise ValidationError(_("Unknown QType"))
    elif (instance.qtype == RADIOBUTTON and (cntCB + cntLL) > 0) or \
        (instance.qtype == CHECKBOX and (cntRB + cntLL) > 0) or \
        (instance.qtype == LINKEDLISTS and (cntRB + cntCB) > 0) :
        raise ValidationError("Нельзя изменять тип вопроса, если вопрос всё ещё имеет ответы.")

pre_save.connect(question_pre_save, sender=Question)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    content = models.TextField()
    ordernum = models.PositiveIntegerField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    qtype = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE_CHOICES,
        default=RADIOBUTTON,
    )

    class Meta:
        verbose_name = 'Простой Ответ'
        verbose_name_plural = 'Простые Ответы'

    def __str__(self):
        return self.content


def answer_pre_save(instance, **kwargs):
    instance.qtype = instance.question.qtype

pre_save.connect(answer_pre_save, sender=Answer)


class AnswerRB(Answer):
    """ qtype == RB
        необходим для создания отдельных валидаторов
    """
    answer = models.OneToOneField(
        Answer, on_delete=models.CASCADE,
        parent_link=True,
    )

    class Meta:
        verbose_name = 'Одиночный Ответ (RadioButton)'
        verbose_name_plural = 'Одиночные Ответы (RadioButton)'

    def clean(self):
        qtype = self.question.qtype
        if qtype != 'RB':
            raise ValidationError("Тип вопроса ({}) и тип ответа (RB) не совпадают.".format(qtype))


class AnswerCB(Answer):
    """ qtype == CB
        необходим для создания отдельных валидаторов
    """
    answer = models.OneToOneField(
        Answer, on_delete=models.CASCADE,
        parent_link=True,
    )

    class Meta:
        verbose_name = 'Множественный Ответ (CheckBox)'
        verbose_name_plural = 'Множественные Ответы (CheckBox)'

    def clean(self):
        qtype = self.question.qtype
        if qtype != 'CB':
            raise ValidationError("Тип вопроса ({}) и тип ответа (CB) не совпадают.".format(qtype))


class AnswerLL(Answer):
    answer = models.OneToOneField(
        Answer, on_delete=models.CASCADE,
        parent_link=True,
    )
    linkeditem = models.TextField()
    ordernumitem = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Ответ-Путанка'
        verbose_name_plural = 'Ответы-Путанки'

    def clean(self):
        qtype = self.question.qtype
        if qtype != 'LL':
            raise ValidationError("Тип вопроса ({}) и тип ответа (LL) не совпадают.".format(qtype))
