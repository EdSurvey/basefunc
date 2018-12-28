from ..clients import install

from ..clients.install import division_the_site, site1_user, site2_user
from questions.models import Question, Answer, AnswerRB, AnswerCB, AnswerLL, RADIOBUTTON, CHECKBOX, LINKEDLISTS

#   setup.questions.install

site_q1 = Question.objects.create(
    name='Unit1 - 1.1',
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
    name='Unit2 - 1.1',
    description="""Choose the two verbs which can be used with the noun 'Data':""",
    division=division_the_site,
    public=True,
    qtype=CHECKBOX,
    owner=site1_user,
)
site_q2_answer1 = AnswerCB.objects.create(
    question=site_q2,
    content="""collect""",
    ordernum=1,
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
    name='Unin9 - 1.1',
    description="""Match the words to make phrases connected to selling:""",
    division=division_the_site,
    public=True,
    qtype=LINKEDLISTS,
    owner=site1_user,
    active=False
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


site_q4 = Question.objects.create(
    name='Unit9 - 4.1',
    description="""Choice one of te words to complete the sentence.
    The ___ should not trade any products that are poor quality.""",
    division=division_the_site,
    public=False,
    qtype=RADIOBUTTON,
    owner=site1_user,
)
site_q4_answer1 = AnswerRB.objects.create(
    question=site_q4,
    content="""buyer""",
    ordernum=None,
    score=1,
    qtype=site_q4.qtype,
)
site_q4_answer2 = AnswerRB.objects.create(
    question=site_q4,
    content="""seller""",
    ordernum=None,
    score=10,
    qtype=site_q4.qtype,
)
site_q4_answer3 = AnswerRB.objects.create(
    question=site_q4,
    content="""warehouse""",
    ordernum=None,
    score=1,
    qtype=site_q4.qtype,
)

site_q5 = Question.objects.create(
    name='Unit9 - 3.1',
    description="""Choose the word that belong in the group.""",
    division=division_the_site,
    public=False,
    qtype=CHECKBOX,
    owner=site1_user,
)
site_q5_answer1 = AnswerCB.objects.create(
    question=site_q5,
    content="""trader""",
    ordernum=None,
    score=10,
    qtype=site_q5.qtype,
)
site_q5_answer2 = AnswerCB.objects.create(
    question=site_q5,
    content="""retailer""",
    ordernum=None,
    score=10,
    qtype=site_q5.qtype,
)
site_q5_answer3 = AnswerCB.objects.create(
    question=site_q5,
    content="""client""",
    ordernum=None,
    score=1,
    qtype=site_q5.qtype,
)

site_q6 = Question.objects.create(
    name='Unit9 - 3.2',
    description="""Choose the word that belong in the group.""",
    division=division_the_site,
    public=False,
    qtype=CHECKBOX,
    owner=site2_user,
)
site_q6_answer1 = AnswerCB.objects.create(
    question=site_q6,
    content="""vendor""",
    ordernum=None,
    score=1,
    qtype=site_q6.qtype,
)
site_q6_answer2 = AnswerCB.objects.create(
    question=site_q6,
    content="""commercial""",
    ordernum=None,
    score=5,
    qtype=site_q6.qtype,
)
site_q6_answer3 = AnswerCB.objects.create(
    question=site_q6,
    content="""advertisment""",
    ordernum=None,
    score=5,
    qtype=site_q6.qtype,
)

site_q7 = Question.objects.create(
    name='Unit9 - 3.3',
    description="""Choose the word that belong in the group.""",
    division=division_the_site,
    public=True,
    qtype=CHECKBOX,
    owner=site2_user,
)
site_q7_answer1 = AnswerCB.objects.create(
    question=site_q7,
    content="""customer""",
    ordernum=None,
    score=5,
    qtype=site_q7.qtype,
)
site_q7_answer2 = AnswerCB.objects.create(
    question=site_q7,
    content="""pay for""",
    ordernum=None,
    score=1,
    qtype=site_q7.qtype,
)
site_q7_answer3 = AnswerCB.objects.create(
    question=site_q7,
    content="""consumer""",
    ordernum=None,
    score=5,
    qtype=site_q7.qtype,
)
