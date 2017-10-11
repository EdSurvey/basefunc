# from ..questions import uninstall

from clients.models import Client


Client.objects.all().delete()