from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # model = Question
    list_display = ('id', 'name', 'description', 'qtype')
    ordering = ('id',)
    fieldsets = [
        (None, {'fields': ['name', 'description', 'qtype',]}),
        ('Приватность', {'fields': ['division', 'public', 'owner',]}),
    ]

admin.site.register(Question, QuestionAdmin)