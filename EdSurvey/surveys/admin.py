from django.contrib import admin

from .models import Anketa


# !!! В проде не будет админки, так как это будет приложение для пользователей !!!

class AnketaAdmin(admin.ModelAdmin):
    model = Anketa

admin.site.register(Anketa, AnketaAdmin)