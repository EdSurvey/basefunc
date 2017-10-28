from django.contrib import admin

from .models import QueryList, QueryContent


@admin.register(QueryList)
class QueryListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'division', 'public')


@admin.register(QueryContent)
class QueryContentAdmin(admin.ModelAdmin):
    list_display = ('querylist', 'question', 'ordernum')