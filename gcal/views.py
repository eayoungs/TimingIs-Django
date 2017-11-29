from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from .models import CalEvent


class AboutView(TemplateView):
    template_name = "gcal/about.html"


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
