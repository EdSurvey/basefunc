from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from clients.models import Person
from .models import Question
#, RADIOBUTTON, CHECKBOX, LINKEDLISTS, Answer, AnswerRB, AnswerCB, AnswerLL


@login_required(login_url='login')
def index(request):
    """ Отображает список доступных вопросов

    Доступны фильтры:
    - public
    - private
    - My

    Для всех моих - отображает кнопки [просмотреть],[изменить],[удалить]
    Для чужих public - отображает только кнопку [просмотреть]
    """
    # person = Person.objects.get(pk=request.session['person_id'])
    questions = Question.objects.all()
    return render(
        request,
        'questions.html',
        {'questions': questions},
    )
