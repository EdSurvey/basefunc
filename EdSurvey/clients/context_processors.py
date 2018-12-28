# clients.context_processors


def person(request):
    """ Returns context variables required by apps that use personalization system.

    If there is no 'person' attribute in the request, uses None.
    """
    if hasattr(request, 'person'):
        person = request.person
    else:
        person = None

    return {
        'person': person,
    }
