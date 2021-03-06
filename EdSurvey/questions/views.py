from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib import messages

from .models import Question, RADIOBUTTON, CHECKBOX, LINKEDLISTS, Answer, AnswerRB, AnswerCB, AnswerLL, get_answer_class, copy_answers
from .forms import EditQuestionForm, EditAnswerForm, EditAnswerFormLL

#   questions.views


DEFAULT_FILTER = (True, True, False, True, True, False)


def is_readonly(request, question):
    return not question.owner == request.person


class Filter:

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

    def render_filter_form(self):
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
        def add_in_filt(filt, expr: bool, item: Q):
            if expr:
                if filt is None:
                    return item
                else:
                    return filt | item
            else:
                return filt

        result = {'include': None, 'exclude': None}
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
    filt = Filter()
    filt.read_session(request)
    person = request.person
    clauses = filt.gen_filter_clause(request)
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
            filt.read_form(request)
        elif request.POST.get("default"):
            filt.__setstate__(DEFAULT_FILTER)
        elif request.POST.get("set_all"):
            filt = Filter()
        filt.write_session(request)
        return redirect(reverse("questions:index"))

    return render(
        request,
        'questions.html',
        {
            'questions': questions,
            'questions_filter_block': filt.render_filter_form(),
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
    """ Форма редактирования/просмотра Вопроса.

    Вызывается при создании нового и редактирования существующего Вопроса.
    """
    readonly = is_readonly(request, question)

    # Get answers of the question.
    answers = None
    if question.id:
        if question.qtype in [RADIOBUTTON, CHECKBOX]:
            answers = Answer.objects.filter(question=question).order_by('ordernum')
        elif question.qtype in [LINKEDLISTS]:
            answers = AnswerLL.objects.filter(question=question).order_by('ordernum', 'ordernumitem')
    has_answers = answers and len(answers) > 0

    if request.method == 'POST':
        if request.POST.get('cancel'):
            return redirect(reverse("questions:index"))
        if request.POST.get('copy') and not question.owner == request.person:   # Чужой вопрос создаём из записи в БД
            copy_question = Question.objects.create(
                name='(new)' + question.name,
                description=question.description,
                qtype=question.qtype,
                division=request.person.division,
                owner=request.person,
                active=False,
                archived=False,
            )
            if has_answers:
                copy_answers(source=question, target=copy_question)
            return redirect(reverse("questions:index"))
        form = EditQuestionForm(request.POST, instance=question, readonly=readonly, answers=has_answers)
        if form.is_valid():
            if request.POST.get('save'):
                try:
                    form.save(commit=True)
                except ValidationError as e:
                    messages.add_message(request, messages.ERROR, e.message)
                    return redirect(request.path)
            elif request.POST.get('copy'):   # Создать новый как копию текущего без сохранения изменений текущего.
                if question.owner == request.person:    # Свой вопрос создаём из формы
                    copy_question = Question.objects.create(
                        name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        qtype=form.cleaned_data['qtype'],
                        division=request.person.division,
                        owner=request.person,
                        active = False,
                        archived = False,
                    )
                    if has_answers:
                        copy_answers(source=question, target=copy_question)
            elif request.POST.get('del'):   # Удалить не связанные и архивирвоать связанные.
                if has_answers:
                    question.archived = True
                    question.active = False
                    try:
                        question.save()
                    except ValidationError as e:
                        messages.add_message(request, messages.ERROR, e.message)
                        return redirect(request.path)
                else:
                    try:
                        question.delete()
                    except ValidationError as e:
                        messages.add_message(request, messages.ERROR, e.message)
                        return redirect(request.path)

            return redirect(reverse("questions:index"))
    else:
        form = EditQuestionForm(instance=question, readonly=readonly, answers=has_answers)

    return render(
        request,
        "editquestion.html",
        {
            'question': question,
            'form': form,
            'answersblock': answers_block(question, answers),
            'readonly': readonly,
        }
    )


def answers_block(question, answers):
    if question.id:
        return render_to_string(
            'answersblock.html',
            {
                'question': question,
                'answers': answers,
            }
        )
    else:
        return ''


@login_required(login_url='login')
def new_answer(request, questionid):
    question = get_object_or_404(Question.with_perms.all(request.person), pk=questionid)
    answer = get_answer_class(question.qtype)()
    answer.question = question
    answer.qtype = question.qtype
    answer.content = "новое содержание"
    return form_answer(request, answer)


@login_required(login_url='login')
def edit_answer(request, answerid):
    answer = get_object_or_404(Answer, pk=answerid)
    if answer.check_perm(request.person):
        return form_answer(request, get_answer_class(answer.qtype).objects.get(answer=answer))
    else:
        raise ObjectDoesNotExist


def form_answer(request, answer):
    readonly = is_readonly(request, answer.question)

    if answer.qtype == 'LL':
        # answer_inst = AnswerLL.objects.get(answer=answer)
        form_class = EditAnswerFormLL
    elif answer.qtype == 'RB':
        # answer_inst = AnswerRB.objects.get(answer=answer)
        form_class = EditAnswerForm
    elif answer.qtype == 'CB':
        # answer_inst = AnswerCB.objects.get(answer=answer)
        form_class = EditAnswerForm

    if request.method == 'POST':
        if request.POST.get('cancel'):
            return redirect(reverse("questions:editquestion", args=[answer.question.id]))
        form = form_class(request.POST, instance=answer)
        if form.is_valid():
            if request.POST.get('save'):
                try:
                    form.save(commit=True)
                except ValidationError as e:
                    messages.add_message(request, messages.ERROR, e.message)
                    return redirect(request.path)
            elif request.POST.get('del'):
                if not answer.question.archived:
                    try:
                        answer.delete()
                    except ValidationError as e:
                        messages.add_message(request, messages.ERROR, e.message)
                        return redirect(request.path)
            return redirect(reverse("questions:editquestion", args=[answer.question.id]))
    else:
        form = form_class(instance=answer)
        if readonly:
            for field in form.fields:
                form.fields[field].widget.attrs['disabled'] = 'disabled'

    return render(
        request,
        "editanswer.html",
        {
            'question': answer.question,
            'form': form,
            'answer': answer,
            'readonly': readonly,
        }
    )
