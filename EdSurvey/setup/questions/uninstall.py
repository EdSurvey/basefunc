# from ..querylists import uninstall

from questions.models import AnswerLL, AnswerCB, AnswerRB, Answer, Question

AnswerLL.objects.all().delete()
AnswerCB.objects.all().delete()
AnswerRB.objects.all().delete()
Answer.objects.all().delete()
Question.objects.all().delete()
