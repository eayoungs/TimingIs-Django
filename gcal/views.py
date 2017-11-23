from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from .models import CalEvent


def index(request):
    template = loader.get_template("gcal/index.html")
    return HttpResponse(template.render())


def events_list(request):
    current_events_list = CalEvent.objects.order_by()
    context = {
        'current_events_list': current_events_list,
    }
    template = loader.get_template('gcal/events_list.html')
    return HttpResponse(template.render(context, request))
