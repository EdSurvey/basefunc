from django.contrib import admin

from .models import Task, Schedule, Attempt


# class ScheduleAdmin(admin.TabularInline):
class ScheduleAdmin(admin.StackedInline):
    model = Schedule
    fieldsets = [
        (None, {'fields': ['name', 'squads', 'start', 'finish', 'owner', 'description',]}),
    ]
    extra = 1  # how many rows to show


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'querylist','division', 'owner',)
    ordering = ('name', 'querylist')
    fieldsets = [
        (None, {'fields': ['name', 'querylist', 'description',]}),
        ('Доступы', {'fields': ['division', 'owner', 'public',]}),
        ('Параметры', {'fields': ['attempts', 'editable', 'viewable', 'autoclose',]})
    ]
    inlines = [
        ScheduleAdmin,
    ]


admin.site.register(Task, TaskAdmin)


class AttemptAdmin(admin.ModelAdmin):
    ordering = ('schedule', '-started')


admin.site.register(Attempt, AttemptAdmin)
