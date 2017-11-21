from django.http import HttpResponse
from django.template import loader

from .models import CalEvent


def index(request):
    current_events_list = CalEvent.objects.order_by()
    context = {
        'current_events_list': current_events_list,
    }
    template = loader.get_template('gcal/index.html')
    return HttpResponse(template.render(context, request))
