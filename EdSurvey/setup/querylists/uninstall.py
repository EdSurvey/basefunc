# from ..schedules import uninstall

from querylists.models import QueryContent, QueryList

QueryContent.objects.all().delete()
QueryList.objects.all().delete()
