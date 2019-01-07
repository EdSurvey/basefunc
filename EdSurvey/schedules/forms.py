from django.forms import ModelForm

from .models import Task, Schedule

#   schedules.forms


class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            # 'querylist',
            'name', 'description',
            'attempts', 'viewable', 'editable', 'autoclose',
            'public', 'active', 'archived',
        ]   # , 'division', 'owner']

    def __init__(self, *args, **kwargs):
        if 'readonly' in kwargs:
            self.readonly = kwargs.pop('readonly')
        else:
            self.readonly = False

        super().__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.pk and self.readonly:
            for field in self.fields:
                self.fields[field].widget.attrs['disabled'] = True


class EditScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = [
            # 'task',
            'name', 'description', 'start', 'finish',
        ]