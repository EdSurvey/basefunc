from surveys.models import ResultLL, Result, Anketa

ResultLL.objects.all().delete()
Result.objects.all().delete()
Anketa.objects.all().delete()
