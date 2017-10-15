from ..clients import install

from ..clients.install import division_the_site, site1_user, site2_user
from questions.models import Question, Answer, AnswerRB, AnswerCB, AnswerLL, RADIOBUTTON, CHECKBOX, LINKEDLISTS

#   setup.questions.install

site_q1 = Question.objects.create(
    name='Unit1 - Reading 1.1',
    description="""The writer thinks that self-service is a good idea for:""",
    division=division_the_site,
    public=True,
    qtype=RADIOBUTTON,
    owner=site1_user,
)
site_q1_answer1 = AnswerRB.objects.create(
    question=site_q1,
    content="""companies not customers""",
    ordernum=1,
    score=1,
    qtype=site_q1.qtype,
)
site_q1_answer2 = AnswerRB.objects.create(
    question=site_q1,
    content="""customers not companies""",
    ordernum=2,
    score=5,
    qtype=site_q1.qtype,
)
site_q1_answer3 = AnswerRB.objects.create(
    question=site_q1,
    content="""both customers and companies""",
    ordernum=3,
    score=10,
    qtype=site_q1.qtype,
)

site_q2 = Question.objects.create(
    name='Unit2 - Underline 1.1',
    description="""Choose the two verbs which can be used with the noun 'Data':""",
    division=division_the_site,
    public=True,
    qtype=CHECKBOX,
    owner=site1_user,
)
site_q2_answer1 = AnswerCB.objects.create(
    question=site_q2,
    content="""collect""",
    ordernum=None,
    score=10,
    qtype=site_q2.qtype,
)
site_q2_answer2 = AnswerCB.objects.create(
    question=site_q2,
    content="""analyze""",
    ordernum=None,
    score=10,
    qtype=site_q2.qtype,
)
site_q2_answer3 = AnswerCB.objects.create(
    question=site_q2,
    content="""advise""",
    ordernum=None,
    score=1,
    qtype=site_q2.qtype,
)

site_q3 = Question.objects.create(
    name='Unin9 - Vocabulary 1.1',
    description="""Match the words to make phrases connected to selling:""",
    division=division_the_site,
    public=False,
    qtype=LINKEDLISTS,
    owner=site1_user,
)
site_q3_answer1 = AnswerLL.objects.create(
    question=site_q3,
    content="""sales""",
    ordernum=1,
    score=10,
    qtype=site_q3.qtype,
    linkeditem="""promotions""",
    ordernumitem=None,
)
site_q3_answer2 = AnswerLL.objects.create(
    question=site_q3,
    content="""sposorship""",
    ordernum=2,
    score=10,
    qtype=site_q3.qtype,
    linkeditem="""deal""",
    ordernumitem=None,
)
site_q3_answer3 = AnswerLL.objects.create(
    question=site_q3,
    content="""advertising""",
    ordernum=3,
    score=10,
    qtype=site_q3.qtype,
    linkeditem="""media""",
    ordernumitem=None,
)
site_q3_answer4 = AnswerLL.objects.create(
    question=site_q3,
    content="""direct""",
    ordernum=4,
    score=10,
    qtype=site_q3.qtype,
    linkeditem="""marketing""",
    ordernumitem=None,
)
site_q3_answer5 = AnswerLL.objects.create(
    question=site_q3,
    content="""public""",
    ordernum=5,
    score=10,
    qtype=site_q3.qtype,
    linkeditem="""relations""",
    ordernumitem=None,
)
site_q3_answer6 = AnswerLL.objects.create(
    question=site_q3,
    content="""personal""",
    ordernum=6,
    score=10,
    qtype=site_q3.qtype,
    linkeditem="""selling""",
    ordernumitem=None,
)


# site_q4 = Question.objects.create(
#     name='что важно котам',
#     description="""Перечислилте то, что главное для котов:""",
#     division=division_the_site,
#     public=True,
#     qtype=CHECKBOX,
#     owner=site1_user,
# )
# site_q4_answer1 = AnswerCB.objects.create(
#     question=site_q4,
#     content="""Хозяин""",
#     ordernum=None,
#     score=5,
#     qtype=site_q4.qtype,
# )
