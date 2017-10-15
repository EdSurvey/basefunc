from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from clients.models import Person
from .models import Question, RADIOBUTTON, CHECKBOX, LINKEDLISTS, Answer, AnswerLL #, AnswerRB, AnswerCB

#   questions.views


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

def answers_by_question(request, questionid):
    question = get_object_or_404(Question, pk=questionid)
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
