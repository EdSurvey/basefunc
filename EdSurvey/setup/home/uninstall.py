from ..clients import uninstall

from django.contrib.auth.models import User, Group

Group.objects.all().delete()
User.objects.all().filter(is_superuser=False).delete()
