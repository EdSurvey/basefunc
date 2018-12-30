from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'querylist','division', 'owner',)
    ordering = ('name', 'querylist')
    fieldsets = [
        (None, {'fields': ['name', 'querylist', 'description',]}),
        ('Доступы', {'fields': ['division', 'owner', 'public',]}),
        ('Параметры', {'fields': ['attempts', 'editable', 'viewable', 'autoclose',]})
    ]
    # inlines = [
    #     ScheduleAdmin,
    # ]


admin.site.register(Task, TaskAdmin)