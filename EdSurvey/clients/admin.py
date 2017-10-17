from django.contrib import admin

from .models import Client, Division, ClientData, Role, Person, Squad

#   clients.admin


class DivisionAdmin(admin.TabularInline):
    model = Division
    ordering = ('shortname',)
    fieldsets = [
        (None, {'fields': ['shortname', 'name',]}),
        ('Параметры', {'fields': ['public', 'private',]})
    ]
    extra = 1  # how many rows to show


class ClientDataAdmin(admin.TabularInline):
    model = ClientData
    fieldsets = [
        (None, {'fields': ['client', 'rootdivision', 'fullname', 'address',]})
    ]
    extra = 1  # how many rows to show


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('id', 'shortname', 'name')
    inlines = [
        DivisionAdmin,
        ClientDataAdmin,
    ]

admin.site.register(Client, ClientAdmin)


class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display = ('name', 'shortname', 'description')

admin.site.register(Role, RoleAdmin)


class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('user', 'shortname', 'division',)   #  'roles',

admin.site.register(Person, PersonAdmin)


class SquadAdmin(admin.ModelAdmin):
    model = Squad

admin.site.register(Squad, SquadAdmin)
