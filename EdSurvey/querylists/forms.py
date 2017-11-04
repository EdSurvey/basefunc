from django.forms import ModelForm

from .models import QueryList, QueryContent

#   querylists.forms


class EditQueryListForm(ModelForm):
    class Meta:
        model = QueryList
        fields = ['name', 'description', 'public', 'active', 'archived']   # , 'division', 'owner']

    def __init__(self, *args, **kwargs):
        if 'readonly' in kwargs:
            self.readonly = kwargs.pop('readonly')
        else:
            self.readonly = False
        if 'contents' in kwargs:
            self.answers = kwargs.pop('contents')
        else:
            self.contents = None

        super().__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.pk and self.readonly:
            for field in self.fields:
                self.fields[field].widget.attrs['disabled'] = True


class EditQueryContentForm(ModelForm):
    class Meta:
        model = QueryContent
        fields = ['ordernum', 'question']
