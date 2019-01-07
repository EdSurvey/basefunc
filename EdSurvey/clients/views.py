#  clients.views
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.timezone import now
from django.urls.base import reverse

from clients.models import Division, Role
from .models import Person


def create_default_person(user):
    person = Person(
        user = user,
        shortname = user.first_name[:15],
        division = Division.objects.get(pk=1),
        role = Role.objects.get(pk=1)
    )
    person.save()
    return person

def touch_person(person):
    person.used = now()
    person.save()


def log_in(request):
    form = AuthenticationForm()
    # form = LoginForm()
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username', ''),
            password=request.POST.get('password', ''),
        )
        if user is not None:
            login(request, user)
            persons = Person.objects.filter(user=user).order_by('-used')[:1]
            cnt = len(persons)
            if cnt < 1:
                active_person = create_default_person(user)
            elif cnt == 1:
                active_person = persons[0]
                touch_person(active_person)
            request.session['person_id'] = active_person.id

            if request.POST.get("Token"):
                token, created = Token.objects.get_or_create(user=user)
                messages.add_message(request, messages.INFO, "Your's token is ".format(token.key))
            try:
                return redirect(request.GET['next'])
            except MultiValueDictKeyError:
                return redirect(reverse('homepage'))
    return render(request,
                  'login.html',
                  {
                      'form': form,
                  })


def log_out(request):
    logout(request)
    return redirect(reverse('homepage'))


def aka(request):
    if request.method == 'POST' and request.POST.get("Ok") and request.POST.get('choice'):
        person_id = request.POST.get('choice')
        person = get_object_or_404(Person, pk=person_id)
        touch_person(person)
        request.session['person_id'] = person.id
        return redirect(reverse('homepage'))
    persons = Person.objects.filter(user=request.user)
    return render(request,
                  'aka.html',
                  {
                      'persons': persons,
                  },)
