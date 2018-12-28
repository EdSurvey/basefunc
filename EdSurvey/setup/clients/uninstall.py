from ..questions import uninstall

from clients.models import Client, Division, ClientData, Role, Person, Squad

#   setup.clients.uninstall

print("Clear model clients.Squad")
for squad in Squad.objects.all():
    squad.delete()
print("Clear model clients.Person")
for person in Person.objects.all():
    person.roles.all().delete()
    person.delete()
print("Clear model clients.Role")
Role.objects.all().delete()
print("Clear model clients.ClientData")
ClientData.objects.all().delete()
print("Clear model clients.Division")
Division.objects.all().delete()
print("Clear model clients.Client")
Client.objects.all().delete()
