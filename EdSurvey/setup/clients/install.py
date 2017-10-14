from ..home import install

#
#   clients Client
#
from clients.models import Client

client_the_site = Client.objects.create(
    id=0,
    name='Education by survey',
    shortname='THE SITE',
    corporate=True,
    public=True,
)

#
#   clients Division
#
from clients.models import Division

division_the_site = Division.objects.create(
    id=0,
    client=client_the_site,
    name=client_the_site.name,
    shortname=client_the_site.shortname,
    public=False,
    private=False,
)
division_the_site_common = Division.objects.create(
    id=1,
    client=client_the_site,
    name='Общедоступные опросы',
    shortname='COMMON',
    public=True,
    private=False,
)

#
#   clients ClientData
#
from clients.models import ClientData

client_the_site_data = ClientData(
    client=client_the_site,
    fullname='Сайт опросов и тестирования',
    address="""Украина, Киев, улица Ивана Мазепы, 3""",
    rootdivision=division_the_site,
)
client_the_site_data.save()

#
#   clients Role
#
from clients.models import Role

role_testee = Role.objects.create(
    id=0,
    name='Тестируемый',
    shortname='TESTEE',
    description="""Предопределённая Роль - могут проходить назначенные и публичные опросы.""",
)
role_user = Role.objects.create(
    id=1,
    name='Пользователь',
    shortname='USER',
    description="""Предопределённая Роль - могут создавать свой персональный контент и использовать публичный.""",
)

#
#   clients Person
#
from clients.models import Person
from ..home.install import user_site1, user_site2

def add_person(user, shortname, division, roles):
    print("Adding: user={}, shortname={}, division={}".format(user, shortname, division))
    print(" roles:", ", ".join(('"{}"'.format(r) for r in roles)))
    person = Person(
        user=user,
        shortname=shortname,
        division=division,
    )
    person.save()
    person.roles.add(*roles)
    return person

site1_user = add_person(
    user=user_site1,
    shortname='Первый',
    division=division_the_site,
    roles=(role_user, role_testee,),
)
site2_user = add_person(
    user=user_site2,
    shortname='Второй',
    division=division_the_site,
    roles=(role_user, role_testee,),
)

#
#   clients Squad
#
from clients.models import Squad
from ..home.install import user_freebee, user_freebee1

def add_squad(name, shortname, description, division, owner, members):
    print("Adding squad: name={}, shortname={}, division={}".format(name, shortname, division))
    print("     members:", ", ".join(('"{}"'.format(r) for r in members)))
    squad = Squad(
        name=name,
        shortname=shortname,
        description=description,
        division=division,
        owner=owner,
    )
    squad.save()
    squad.members.add(*members)
    return squad

squad_site_1 = add_squad(
    name='Тест №1',
    shortname='Тест №1',
    description="""Для проверки базового функционала - первые пользователи""",
    division=division_the_site_common,
    owner=site1_user,
    members=(user_site2, user_freebee,),
)

squad_site_2 = add_squad(
    name='Тест №2',
    shortname='Тест №2',
    description="""Для проверки базового функционала - вторые пользователи""",
    division=division_the_site_common,
    owner=site2_user,
    members=(user_site1, user_freebee1,),
)
