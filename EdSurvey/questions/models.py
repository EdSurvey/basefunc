from django.db import models

from clients.models import Division, Person


RADIOBUTTON = 'RB'  # (*) One -from- List
CHECKBOX = 'CB'  # [v] Some -from- List
LINKEDLISTS = 'LL'  # Link One from first list -to- One from other list
QUESTION_TYPE_CHOICES = (
    (RADIOBUTTON, 'Один из ...'),
    (CHECKBOX, 'Несколько из ...'),
    (LINKEDLISTS, "Путанка"),
)

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

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return "{}.{}.{}".format(self.id, self.qtype, self.name)
