from django import forms
from django.forms import modelformset_factory, BaseModelFormSet, ModelForm, inlineformset_factory

from .models import Question, Answer, AnswerLL

class EditForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'description', 'qtype', 'public', 'active', 'archived', 'division', 'owner']


AnswerFormSet = modelformset_factory(Answer, fields=('content', 'ordernum', 'score'), max_num=1)

AnswerFormSetLL = modelformset_factory(AnswerLL, fields=('content', 'ordernum', 'score', 'linkeditem', 'ordernumitem',), max_num=1)
