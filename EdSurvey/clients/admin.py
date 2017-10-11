#   clients.admin
from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('id', 'shortname', 'name')

admin.site.register(Client, ClientAdmin)
