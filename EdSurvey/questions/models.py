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

    @staticmethod
    def filter_expr(person):
        return Q(public=True) | (Q(owner=person) & Q(division=person.division))

    def all(self, person):
        return super().get_queryset().filter(self.filter_expr(person))


class Question(models.Model):
    name = models.CharField('наименование', max_length=60)
    description = models.TextField('полное описание')
    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name='организация')
    public = models.BooleanField('публичный', default=False)
    qtype = models.CharField(max_length=2,
                             choices=QUESTION_TYPE_CHOICES,
                             default=RADIOBUTTON,
                             verbose_name='Тип вопроса',
                             blank=True)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name='личность-владелец')
    active = models.BooleanField('активный', default=True)
    archived = models.BooleanField('архивный', default=False)

    objects = models.Manager()
    with_perms = QuestionManager()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return "{}.{}.{}".format(self.id, self.qtype, self.name)

    def __setstate__(self, state):
        self.name = state['name']
        self.description = state['description']
        self.qtype = state['qtype']
        self.public = state['public']
        self.active = state['active']
        self.division = state['division']
        self.owner = state['owner']


def question_pre_save(instance, **kwargs):
    # Проверка на изменение типа вопроса (qtype)
    # select 1 from Answer where Answer.question = self.id limit 1
    cntRB = AnswerRB.objects.all().filter(question=instance)[:1].count()
    cntCB = AnswerCB.objects.all().filter(question=instance)[:1].count()
    cntLL = AnswerLL.objects.all().filter(question=instance)[:1].count()
    if instance.qtype not in [qtype for (qtype, txt) in QUESTION_TYPE_CHOICES]:
        raise ValidationError(_("Unknown QType"))
    elif (instance.qtype == RADIOBUTTON and (cntCB + cntLL) > 0) or \
        (instance.qtype == CHECKBOX and (cntRB + cntLL) > 0) or \
        (instance.qtype == LINKEDLISTS and (cntRB + cntCB) > 0):
        raise ValidationError("Нельзя изменять тип вопроса, если вопрос всё ещё имеет ответы.")

pre_save.connect(question_pre_save, sender=Question)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='вариант')
    content = models.TextField(verbose_name='вариант')
    ordernum = models.PositiveIntegerField(null=True, blank=True, verbose_name='порядок варианта')
    score = models.PositiveIntegerField(null=True, blank=True, verbose_name='балл')
    qtype = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE_CHOICES,
        default=RADIOBUTTON,
        verbose_name = 'тип вопроса',
    )

    class Meta:
        verbose_name = 'Простой вариант'
        verbose_name_plural = 'Простые варианты'

    def __str__(self):
        return self.content

    def check_perm(self, person):
        return Question.with_perms.all(person).filter(pk=self.question.id)[:1].count() == 1

    def __getstate__(self):
        return {
            'content': self.content,
            'ordernum': self.ordernum,
            'score': self.score,
            'qtype': self.qtype,
        }

    def __setstate__(self, state):
        self.content, self.ordernum, self.score, self.qtype = \
            state['content'], state['ordernum'], state['score'], state['qtype']



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
        verbose_name = 'Одиночный вариант (RadioButton)'
        verbose_name_plural = 'Одиночные варианты (RadioButton)'

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
        verbose_name = 'Множественный вариант (CheckBox)'
        verbose_name_plural = 'Множественные варианты (CheckBox)'

    def clean(self):
        qtype = self.question.qtype
        if qtype != 'CB':
            raise ValidationError("Тип вопроса ({}) и тип ответа (CB) не совпадают.".format(qtype))


class AnswerLL(Answer):
    answer = models.OneToOneField(
        Answer, on_delete=models.CASCADE,
        parent_link=True,
    )
    linkeditem = models.TextField(verbose_name='ответ')
    ordernumitem = models.PositiveIntegerField(null=True, blank=True, verbose_name='порядок ответа')

    class Meta:
        verbose_name = 'Ответ-Путанка'
        verbose_name_plural = 'Ответы-Путанки'

    def clean(self):
        qtype = self.question.qtype
        if qtype != 'LL':
            raise ValidationError("Тип вопроса ({}) и тип ответа (LL) не совпадают.".format(qtype))

    def __getstate__(self):
        result = super().__getstate__()
        result['linkeditem'] = self.linkeditem
        result['ordernumitem'] = self.ordernumitem
        return result

    def __setstate__(self, state):
        self.linkeditem, self.ordernumitem = \
            state['linkeditem'], state['ordernumitem']


def get_answer_class(qtype):
    if qtype == 'LL':
        return AnswerLL
    elif qtype == 'RB':
        return AnswerRB
    elif qtype == 'CB':
        return AnswerCB


def copy_answers(source, target):
    """ Copy answers of source Question to target Question

    :param source: saved Question
    :param target: sqved Question
    :return:
    """
    answer_class = get_answer_class(source.qtype)
    for source_answer in answer_class.objects.filter(question=source):
        # Create new instance of Answer*
        target_answer = answer_class()
        # Link create new instance of Answer* to target Question
        target_answer.question = target
        # Copy source attribute values into target ones
        target_answer.__setstate__(source_answer.__getstate__())
        target_answer.save()
