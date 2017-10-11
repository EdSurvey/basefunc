# from ..questions import uninstall

from clients.models import Client, Division, ClientData


ClientData.objects.all().delete()
Division.objects.all().delete()
Client.objects.all().delete()