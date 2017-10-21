from django.forms import ModelForm

from .models import Question, Answer, AnswerLL

class EditForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'description', 'qtype', 'public', 'active', 'archived', 'division', 'owner']


class EditAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'ordernum', 'score']


class EditAnswerFormLL(ModelForm):
    class Meta:
        model = AnswerLL
        fields = ['content', 'ordernum', 'score', 'linkeditem', 'ordernumitem',]

