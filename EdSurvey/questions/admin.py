from django.contrib import admin

from .models import Question, Answer, AnswerRB, AnswerCB, AnswerLL


class AnswerAdmin(admin.ModelAdmin):
    # list_display = ('id', 'question', 'score', 'ordernum', 'content')
    model = Answer


class AnswerRBAdmin(admin.TabularInline):
    # list_display = ('id', 'question', 'score', 'ordernum', 'content')
    model = AnswerRB
    extra = 1  # how many rows to show


# admin.site.register(AnswerRB, AnswerRBAdmin)


class AnswerCBAdmin(admin.TabularInline):
    # list_display = ('id', 'question', 'score', 'ordernum', 'content')
    model = AnswerCB
    extra = 1  # how many rows to show


class AnswerLLAdmin(admin.TabularInline):
    # list_display = ('id', 'question', 'score', 'ordernum', 'content', 'linkeditem', 'ordernumitem')
    model = AnswerLL
    extra = 1  # how many rows to show


class QuestionAdmin(admin.ModelAdmin):
    # model = Question
    list_display = ('id', 'name', 'description', 'qtype')
    ordering = ('id',)
    fieldsets = [
        (None, {'fields': ['name', 'description', 'qtype',]}),
        ('Приватность', {'fields': ['division', 'owner', 'public', 'active',]}),
    ]
    inlines = [
        AnswerRBAdmin,
        AnswerCBAdmin,
        AnswerLLAdmin,
    ]


admin.site.register(Question, QuestionAdmin)