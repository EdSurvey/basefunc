from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from clients.models import Person
from .models import Question, RADIOBUTTON, CHECKBOX, LINKEDLISTS, Answer, AnswerLL #, AnswerRB, AnswerCB

#   questions.views


def render_filter_form(request):
    return render_to_string(
        'questionsfilterblock.html',
        {'flt_q_pub': request.session['flt_q_pub'],
         'flt_q_own': request.session['flt_q_own'],
         'flt_q_oth': request.session['flt_q_oth'],
         'flt_q_act': request.session['flt_q_act'],
         'flt_q_arc': request.session['flt_q_arc']}
    )


def gen_filter_clause(request):

    def add_in_filt(filt, expr:bool, item:Q):
        if expr:
            if filt is None:
                return item
            else:
                return filt | item
        else:
            return filt

    result = {'include':None, 'exclude':None}
    result['exclude'] = add_in_filt(result['exclude'], not request.session['flt_q_pub'], Q(public=True) & Q(owner=request.person))
    result['exclude'] = add_in_filt(result['exclude'], not request.session['flt_q_own'], Q(owner=request.person))
    result['include'] = add_in_filt(result['include'], not request.session['flt_q_oth'], Q(owner=request.person))
    result['exclude'] = add_in_filt(result['exclude'], not request.session['flt_q_act'], Q(active=True))
    result['exclude'] = add_in_filt(result['exclude'], not request.session['flt_q_arc'], Q(active=False))
    return result

def set_filter_default(request):
    if 'flt_q_pub' not in request.session:
        request.session['flt_q_pub'] = True
    if 'flt_q_own' not in request.session:
        request.session['flt_q_own'] = True
    if 'flt_q_oth' not in request.session:
        request.session['flt_q_oth'] = False
    if 'flt_q_act' not in request.session:
        request.session['flt_q_act'] = True
    if 'flt_q_arc' not in request.session:
        request.session['flt_q_arc'] = False

@login_required(login_url='login')
def index(request):
    """ Отображает список доступных вопросов

    Доступны фильтры:
    - public
    - private
    - My
    - Others
    - Active
    - Archive

    Для всех моих - отображает кнопки [просмотреть],[изменить],[удалить]
    Для чужих public - отображает только кнопку [просмотреть]
    """
    set_filter_default(request)
    person = request.person
    clauses = gen_filter_clause(request)
    questions = Question.with_perms.all(person)
    if clauses['include'] and clauses['exclude']:
        questions = questions.filter(clauses['include']).exclude(clauses['exclude'])
    elif clauses['include']:
        questions = questions.filter(clauses['include'])
    elif clauses['exclude']:
        questions = questions.exclude(clauses['exclude'])
    # questions = Question.with_perms.all(person)
    return render(
        request,
        'questions.html',
        {'questions': questions,
         'questions_filter_block': render_filter_form(request)},
    )

@login_required(login_url='login')
def answers_by_question(request, questionid):
    question = get_object_or_404(Question.with_perms.all(request.person), pk=questionid)
    if question.qtype in [RADIOBUTTON, CHECKBOX]:
        answers = Answer.objects.filter(question=question)
        return render(
            request,
            'answersbyquestion.html',
            {'question': question,
             'answers': answers}
        )
    elif question.qtype in [LINKEDLISTS]:
        answers = AnswerLL.objects.filter(question=question)
        return render(
            request,
            'answersllbyquestion.html',
            {'question': question,
             'answers': answers}
        )
