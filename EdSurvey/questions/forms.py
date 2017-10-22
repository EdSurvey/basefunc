from django.forms import ModelForm

from .models import Question, Answer, AnswerLL


class EditQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'description', 'qtype', 'public', 'active', 'archived']   #, 'division', 'owner']

    def __init__(self, *args, **kwargs):
        if 'readonly' in kwargs:
            self.readonly = kwargs.pop('readonly')
        else:
            self.readonly = False
        if 'answers' in kwargs:
            self.answers = kwargs.pop('answers')
        else:
            self.answers = None

        super().__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance:
            if instance.pk:
                if self.readonly:
                    for field in self.fields:
                        self.fields[field].widget.attrs['disabled'] = True
                elif self.answers: # При наличии ответов - нельзя менять тип вопроса.
                    self.fields['qtype'].widget.attrs['disabled'] = True

    def clean_qtype(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk and self.answers:
            return instance.qtype
        else:
            return self.cleaned_data['qtype']

    # def clean_owner(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.owner
    #     else:
    #         return self.cleaned_data['owner']
    #
    # def clean_division(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.division
    #     else:
    #         return self.cleaned_data['division']


class EditAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content', 'ordernum', 'score']


class EditAnswerFormLL(ModelForm):
    class Meta:
        model = AnswerLL
        fields = ['content', 'ordernum', 'score', 'linkeditem', 'ordernumitem']
