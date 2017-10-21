from django import forms
from django.forms import modelformset_factory, BaseModelFormSet, ModelForm, inlineformset_factory

from .models import Question, Answer, AnswerLL

class EditForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'description', 'qtype', 'public', 'active', 'archived', 'division', 'owner']


AnswerFormSet = modelformset_factory(
    Answer,
    fields=('content', 'ordernum', 'score'),
    max_num=1,
    widgets={
        'content': forms.Textarea(attrs={'rows': 3})
    },
)

AnswerFormSetLL = modelformset_factory(
    AnswerLL,
    fields=('content', 'ordernum', 'score', 'linkeditem', 'ordernumitem',),
    max_num=1,
    widgets={
        'content': forms.Textarea(attrs={'rows': 3}),
        'linkeditem': forms.Textarea(attrs={'rows': 3})
    },
)


class EditAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'  # TODO: fields = ['name', 'description', 'qtype', 'public', 'active', 'archived', 'division', 'owner']


class EditAnswerFormLL(ModelForm):
    class Meta:
        model = AnswerLL
        fields = '__all__'  # TODO: fields = ['name', 'description', 'qtype', 'public', 'active', 'archived', 'division', 'owner']
