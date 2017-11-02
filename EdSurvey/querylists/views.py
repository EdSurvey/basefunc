from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from querylists.models import QueryList

#   querylists.views

@login_required(login_url='login')
def index(request):

    querylists = QueryList.objects.all()

    return render(
        request,
        'querylists.html',
        {
            'querylists': querylists,
            # 'questions_filter_block': filt.render_filter_form(),
        },
    )
