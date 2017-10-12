from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.db import models


class Client(models.Model):
    name = models.CharField('название', max_length=60)
    shortname = models.CharField('абревиатура', max_length=30)
    corporate = models.BooleanField('корпорация', default=False)
    public = models.BooleanField('публичный контент', default=True)

    def delete(self, *args, **kwargs):
        if self.id == 1:
            raise ValidationError("Нельзя удалить Корневого Клиента.")
        super(Client, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return self.name


class Division(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    name = models.CharField('название', max_length=60)
    shortname = models.CharField('абревиатура', max_length=15)
    public = models.BooleanField('публичный контент', default=False)
    private = models.BooleanField('контент только этого подразделения', default=False)

    def delete(self, *args, **kwargs):
        if self.id == 0:
            raise ValidationError("Нельзя удалить Корневую организацию Сайта.")
        try:
            clientdata = ClientData.objects.get(client=self.client)
            if clientdata.rootdivision == self:
                raise ValidationError("Нельзя удалить Корневую организацию Клиента.")
        except ObjectDoesNotExist:
            # Если нет доп.данных, то и проблемы нет.
            pass
        super(Division, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'
        unique_together = (
            ('client', 'shortname'),
            ('client', 'name'),
        )

    def __str__(self):
        return self.name


class ClientData(models.Model):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        primary_key=True
        # parent_link=True,
    )
    fullname = models.CharField('полное наименование', max_length=120)
    address = models.TextField('почтовый адрес', null=True, blank=True)
    # domain = models.CharField('корпоративный почтовый домен', null=True, blank=True)
    rootdivision = models.ForeignKey(Division,
                                     on_delete=models.PROTECT,
                                     verbose_name='корневая организация',)
    def save(self, **kwargs):
        # print(self.rootdivision.client.id, self.client.id)
        if self.rootdivision and self.rootdivision.client.id != self.client.id:
            raise ValidationError("Корневое подразделение указано не корректно.")
        super(ClientData, self).save(**kwargs)

    class Meta:
        verbose_name = 'дополнительная информация о Клиенте'
        verbose_name_plural = 'дополнительная информация о Клиентах'


def division_post_save(instance, **kwargs):
    """
    Если это первая организация Клиента,
    то автосоздание и автозаполнение доп.данных Клиента.
    """
    # cnt = Division.objects.all().filter(client=instance.client).count()
    # print(cnt)
    if Division.objects.all().filter(client=instance.client).count() <= 1:
        try:
            clientdata = ClientData.objects.get(client=instance.client)
        except ObjectDoesNotExist:
            ClientData.objects.create(client=instance.client,
                                      fullname=instance.client.name,
                                      rootdivision=instance)

post_save.connect(division_post_save, sender=Division)


class Role(models.Model):
    name = models.CharField('название', max_length=60, unique=True)
    shortname = models.CharField('абревиатура', max_length=30, unique=True)
    description = models.TextField('описание')

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'

    def __str__(self):
        return "{}".format(self.name)


class Person(models.Model):
    """ Личность

    Позволяет создать алиасы Пользователей
    для дальнейшей работы с различными Клиентами
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    shortname = models.CharField('aka', max_length=30)
    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name='входит в организацию')
    # role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name='доступная роль')
    roles = models.ManyToManyField(Role, blank=True, verbose_name='роли')
    used = models.DateTimeField(auto_now_add=now())

    class Meta:
        verbose_name = 'личность'
        verbose_name_plural = 'личности'
        unique_together = (('user', 'shortname',),)

    def __str__(self):
        return '{} {} aka "{}"'.format(self.user.first_name, self.user.last_name, self.shortname)


def get_active_person(request):
    return get_object_or_404(Person, pk=request.session['person_id'])
