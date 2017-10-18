from django import forms
from .models import Question

class EditForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'description', 'qtype', 'public', 'active', 'archived', 'division', 'owner']
