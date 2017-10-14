from django.core.exceptions import ObjectDoesNotExist
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject

from .models import Person


def get_person(request):
    """ Get object Person for request.session['person_id']

    :param request:
    :return: Person(request.session['person_id']) or None for unexpected person_id
    """
    if 'person_id' in request.session:
        person_id = request.session['person_id']
        try:
            return Person.objects.get(pk=person_id)
        except ObjectDoesNotExist:
            pass
    return None


class PersonMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """ Set request.person or clear it. """
        value = SimpleLazyObject(lambda: get_person(request))
        if value:
            request.person = value
        elif hasattr(request, 'person'):
            del request.person
            if 'person_id' in request.session:
                del request.session['person_id']
