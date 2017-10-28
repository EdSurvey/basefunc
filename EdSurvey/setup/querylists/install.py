from ..questions import install

from ..questions.install import site_q1, site_q2, site_q3, site_q4, site_q5, site_q6, site_q7
from ..clients.install import division_the_site, site1_user, site2_user

from querylists.models import QueryList, QueryContent

#   setup.questions.install

querylist1 = QueryList.objects.create(
    name='IB. Intermediate. Unit 1, 2',
    description="""Intelligent Business. Intermediate. Unit 1.

Vocabulary: Activities
Lanuage: Present Simple and Present Continuous
Career skils: Explaining your job
Writing: Email introducing yourself


Unit 2.

Vocabulary: Data
Lanuage: Countable and Uncountable
Career skils: Checking information
Writing: Letter requesting information
""",
    division=division_the_site,
    public=True,
    owner=site1_user,
)
querylist1_question1 = QueryContent.objects.create(
    querylist=querylist1,
    question=site_q1,
    ordernum=1,
)
querylist1_question2 = QueryContent.objects.create(
    querylist=querylist1,
    question=site_q2,
    ordernum=2,
)

querylist2 = QueryList.objects.create(
    name='IB. Intermediate. Unit 9',
    description="""Intelligent Business. Intermediate. Unit 9.

Vocabulary: Selling
Lanuage: Modals of obligation
Career skils: Making suggestions
Writing: Note making a suggestion
""",
    division=division_the_site,
    public=True,
    owner=site1_user,
)
querylist2_question1 = QueryContent.objects.create(
    querylist=querylist2,
    question=site_q3,
    ordernum=None,
)
querylist2_question2 = QueryContent.objects.create(
    querylist=querylist2,
    question=site_q4,
    ordernum=None,
)
querylist2_question3 = QueryContent.objects.create(
    querylist=querylist2,
    question=site_q5,
    ordernum=None,
)
querylist2_question4 = QueryContent.objects.create(
    querylist=querylist2,
    question=site_q6,
    ordernum=None,
)
querylist2_question5 = QueryContent.objects.create(
    querylist=querylist2,
    question=site_q7,
    ordernum=None,
)
