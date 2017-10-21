from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Question, RADIOBUTTON, CHECKBOX, LINKEDLISTS, Answer, AnswerLL #, AnswerRB, AnswerCB
from .forms import EditForm, AnswerFormSet, AnswerFormSetLL, EditAnswerForm, EditAnswerFormLL

#   questions.views


DEFAULT_FILTER = (True, True, False, True, True, False)

class Filter():

    def __init__(self):
        self.pub = self.own = self.oth = self.act = self.hid = self.arc = True

    def __setstate__(self, state):
        self.pub, self.own, self.oth, self.act, self.hid, self.arc = state

    def __getstate__(self):
        return self.pub, self.own, self.oth, self.act, self.hid, self.arc

    def read_session(self, request):
        """ Загрузить атрибуты из session """
        self.__setstate__(DEFAULT_FILTER)
        if 'flt_q_pub' in request.session:
            self.pub = request.session['flt_q_pub']
        if 'flt_q_own' in request.session:
            self.own = request.session['flt_q_own']
        if 'flt_q_oth' in request.session:
            self.oth = request.session['flt_q_oth']
        if 'flt_q_act' in request.session:
            self.act = request.session['flt_q_act']
        if 'flt_q_hid' in request.session:
            self.hid = request.session['flt_q_hid']
        if 'flt_q_arc' in request.session:
            self.arc = request.session['flt_q_arc']

    def write_session(self, request):
        """ Записать атрибуты в session """
        request.session['flt_q_pub'] = self.pub
        request.session['flt_q_own'] = self.own
        request.session['flt_q_oth'] = self.oth
        request.session['flt_q_act'] = self.act
        request.session['flt_q_hid'] = self.hid
        request.session['flt_q_arc'] = self.arc

    def read_form(self, request):
        """ Загрузить атрибуты из формы """
        try:
            self.pub = request.POST.get('choice_pub') is not None
        except KeyError:
            self.pub = DEFAULT_FILTER[0]
        try:
            self.own = request.POST.get('choice_own') is not None
        except KeyError:
            self.own = DEFAULT_FILTER[1]
        try:
            self.oth = request.POST.get('choice_oth') is not None
        except KeyError:
            self.oth = DEFAULT_FILTER[2]
        try:
            self.act = request.POST.get('choice_act') is not None
        except KeyError:
            self.act = DEFAULT_FILTER[3]
        try:
            self.hid = request.POST.get('choice_hid') is not None
        except KeyError:
            self.hid = DEFAULT_FILTER[4]
        try:
            self.arc = request.POST.get('choice_arc') is not None
        except KeyError:
            self.arc = DEFAULT_FILTER[5]

    def render_filter_form(self, request):
        return render_to_string(
            'questionsfilterblock.html',
            {
                'flt_q_pub': self.pub,
                'flt_q_own': self.own,
                'flt_q_oth': self.oth,
                'flt_q_act': self.act,
                'flt_q_hid': self.hid,
                'flt_q_arc': self.arc
            }
        )

    def gen_filter_clause(self, request):
        def add_in_filt(filt, expr:bool, item:Q):
            if expr:
                if filt is None:
                    return item
                else:
                    return filt | item
            else:
                return filt

        result = {'include':None, 'exclude':None}
        result['exclude'] = add_in_filt(result['exclude'], not self.pub, Q(public=True) & Q(owner=request.person))
        result['exclude'] = add_in_filt(result['exclude'], not self.own, Q(owner=request.person))
        result['include'] = add_in_filt(result['include'], not self.oth, Q(owner=request.person))
        result['exclude'] = add_in_filt(result['exclude'], not self.act, Q(active=True))
        result['exclude'] = add_in_filt(result['exclude'], not self.hid, Q(active=False))
        result['exclude'] = add_in_filt(result['exclude'], not self.arc, Q(archived=True))
        return result


@login_required(login_url='login')
def index(request):
    """ Отображает список доступных вопросов

    Для всех моих - отображает кнопки [просмотреть],[изменить],[удалить]
    Для чужих public - отображает только кнопку [просмотреть]
    """
    filter = Filter()
    filter.read_session(request)
    person = request.person
    clauses = filter.gen_filter_clause(request)
    questions = Question.with_perms.all(person)
    if clauses['include'] and clauses['exclude']:
        questions = questions.filter(clauses['include']).exclude(clauses['exclude'])
    elif clauses['include']:
        questions = questions.filter(clauses['include'])
    elif clauses['exclude']:
        questions = questions.exclude(clauses['exclude'])

    if request.method == 'POST':
        if request.POST.get("new"):
            return redirect(reverse("questions:newquestion"))
        elif request.POST.get("filter"):
            filter.read_form(request)
        elif request.POST.get("default"):
            filter.__setstate__(DEFAULT_FILTER)
        elif request.POST.get("set_all"):
            filter = Filter()
        filter.write_session(request)
        return redirect(reverse("questions:index"))

    return render(
        request,
        'questions.html',
        {
            'questions': questions,
            'questions_filter_block': filter.render_filter_form(request),
        },
    )


@login_required(login_url='login')
def new_question(request):
    question = Question()
    question.name = "о чём вопрос"
    question.description = "описание задания и текст вопроса"
    question.division = request.person.division
    question.owner = request.person
    question.active = False
    question.archived = False
    return form_question(request, question)


@login_required(login_url='login')
def edit_question(request, questionid):
    question = get_object_or_404(Question.with_perms.all(request.person), pk=questionid)
    return form_question(request, question)


def form_question(request, question):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=question)
        if form.is_valid():
            if request.POST.get('save'):
                form.save(commit=True)
            elif request.POST.get('del'):   # Удалить не связанные и архивирвоать связанные.
                if Answer.objects.filter(question=question)[:1].count() == 0:
                    question.delete()
                else:
                    question.archived = True
                    question.active = False
                    question.save()
            elif request.POST.get('cancel'):
                pass
            return redirect(reverse("questions:index"))
    else:
        form = EditForm(instance=question)
    # Get answers of the question.
    if question.qtype in [RADIOBUTTON, CHECKBOX]:
        answers = Answer.objects.filter(question=question).order_by('ordernum')
    elif question.qtype in [LINKEDLISTS]:
        answers = AnswerLL.objects.filter(question=question).order_by('ordernum','ordernumitem')

    return render(
        request,
        "editquestion.html",
        {
            'question': question,
            'form': form,
            'answersblock': answers_block(request, question, answers),
        }
    )


def answers_block(request, question, answers):
    return render_to_string(
        'answersblock.html',
        {
            'question': question,
            'answers': answers,
        }
    )


@login_required(login_url='login')
def new_answer(request, questionid):
    question = get_object_or_404(Question.with_perms.all(request.person), pk=questionid)
    answer = Answer()
    answer.question = question
    answer.qtype = question.qtype
    answer.content = "новое содержание"
    return form_answer(request, answer)


@login_required(login_url='login')
def edit_answer(request, answerid):
    answer = get_object_or_404(Answer, pk=answerid)
    if answer.check_perm(request.person):
        return form_answer(request, answer)
    else:
        raise ObjectDoesNotExist


def form_answer(request, answer):
    if answer.qtype == 'LL':
        answer_inst = AnswerLL.objects.get(answer=answer)
        form_class = EditAnswerFormLL
    else:
        answer_inst = answer
        form_class = EditAnswerForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=answer_inst)
        if form.is_valid():
            if request.POST.get('save'):
                form.save(commit=True)
            elif request.POST.get('del'):
                if not answer.question.archived:
                    answer.delete()
            elif request.POST.get('cancel'):
                pass
            return redirect(reverse("questions:editquestion", args=[answer.question.id]))
    else:
        form = form_class(instance=answer_inst)

    return render(
        request,
        "editanswer.html",
        {
            'question': answer.question,
            'form': form,
            'answer': answer,
        }
    )


@login_required(login_url='login')
def answers_by_question(request, questionid):
    question = get_object_or_404(Question.with_perms.all(request.person), pk=questionid)
    if question.qtype in [RADIOBUTTON, CHECKBOX]:
        answers = Answer.objects.filter(question=question).order_by('ordernum')
        formset_class = AnswerFormSet
        answer_template = 'answersbyquestion.html'
    elif question.qtype in [LINKEDLISTS]:
        answers = AnswerLL.objects.filter(question=question).order_by('ordernum','ordernumitem')
        formset_class = AnswerFormSetLL
        answer_template = 'answersllbyquestion.html'

    if request.method == 'POST':
        formset = formset_class(request.POST, request.FILES)
        if request.POST.get('save') and formset.is_valid():
            formset.save()
        return redirect(reverse("questions:index"))
    else:
        formset = formset_class(queryset=answers)

    return render(
        request,
        answer_template,
        {
            'question': question,
            'answers': answers,
            'formset': formset,
        }
    )
