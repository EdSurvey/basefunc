from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.urls.base import reverse
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from querylists.models import QueryList
from .forms import EditQueryListForm

#   querylists.views

DEFAULT_FILTER = (True, True, False, True, True, False)


def is_readonly(request, querylist):
    return not querylist.owner == request.person


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

    filt = Filter()
    filt.read_session(request)
    person = request.person
    clauses = filt.gen_filter_clause(request)
    querylists = QueryList.with_perms.all(person)
    if clauses['include'] and clauses['exclude']:
        querylists = querylists.filter(clauses['include']).exclude(clauses['exclude'])
    elif clauses['include']:
        querylists = querylists.filter(clauses['include'])
    elif clauses['exclude']:
        querylists = querylists.exclude(clauses['exclude'])

    if request.method == 'POST':
        if request.POST.get("new"):
            return redirect(reverse("querylists:newquerylist"))
        elif request.POST.get("filter"):
            filt.read_form(request)
        elif request.POST.get("default"):
            filt.__setstate__(DEFAULT_FILTER)
        elif request.POST.get("set_all"):
            filt = Filter()
        filt.write_session(request)
        return redirect(reverse("querylists:index"))

    return render(
        request,
        'querylists.html',
        {
            'querylists': querylists,
            'querylists_filter_block': filt.render_filter_form(),
        },
    )


@login_required(login_url='login')
def new_querylist(request):
    querylist = QueryList()
    querylist.name = "о чём Опросник"
    querylist.description = "более подробное описание Опросника"
    querylist.division = request.person.division
    querylist.owner = request.person
    querylist.active = False
    querylist.archived = False
    return form_querylist(request, querylist)


@login_required(login_url='login')
def edit_querylist(request, querylistid):
    querylist = get_object_or_404(QueryList.with_perms.all(request.person), pk=querylistid)
    return form_querylist(request, querylist)


def form_querylist(request, querylist):
    """ Форма редактирования/просмотра Опросника.

    Вызывается при создании нового и редактирования существующего Опрсника.
    """
    readonly = is_readonly(request, querylist)

    # TODO: Get QuesryContents of the querylist.
    has_contents = True

    if request.method == 'POST':
        if request.POST.get('cancel'):
            return redirect(reverse("querylist:index"))
        if request.POST.get('copy') and not querylist.owner == request.person:   # Чужой Опрос создаём из записи в БД
            copy_querylist = QueryList.objects.create(
                name='(new)' + querylist.name,
                description=querylist.description,
                division=request.person.division,
                owner=request.person,
                active=False,
                archived=False,
            )
            if has_contents: pass
                # copy_contents(source=question, target=copy_question)
            return redirect(reverse("querylists:index"))
        form = EditQueryListForm(request.POST, instance=querylist, readonly=readonly, contents=has_contents)
        if form.is_valid():
            if request.POST.get('save'):
                try:
                    form.save(commit=True)
                except ValidationError as e:
                    messages.add_message(request, messages.ERROR, e.message)
                    return redirect(request.path)
            elif request.POST.get('copy'):   # Создать новый как копию текущего без сохранения изменений текущего.
                if querylist.owner == request.person:    # Свой вопрос создаём из формы
                    copy_question = QueryList.objects.create(
                        name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        qtype=form.cleaned_data['qtype'],
                        division=request.person.division,
                        owner=request.person,
                        active = False,
                        archived = False,
                    )
                    if has_contents:    pass
                        # copy_answers(source=question, target=copy_question)
            elif request.POST.get('del'):   # Удалить не связанные и архивирвоать связанные.
                if has_contents:
                    querylist.archived = True
                    querylist.active = False
                    try:
                        querylist.save()
                    except ValidationError as e:
                        messages.add_message(request, messages.ERROR, e.message)
                        return redirect(request.path)
                else:
                    try:
                        querylist.delete()
                    except ValidationError as e:
                        messages.add_message(request, messages.ERROR, e.message)
                        return redirect(request.path)

            return redirect(reverse("querylists:index"))
    else:
        form = EditQueryListForm(instance=querylist, readonly=readonly, contents=has_contents)

    return render(
        request,
        "editqlist.html",
        {
            'querylist': querylist,
            'form': form,
            # 'answersblock': answers_block(querylist, answers),
            'readonly': readonly,
        }
    )
