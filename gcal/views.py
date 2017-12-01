from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
#from django.contrib.auth.models import User
from django.shortcuts import render

from .models import CalEvent


class AboutView(TemplateView):
    template_name = "gcal/about.html"


class ContactView(TemplateView):
    template_name = "gcal/contact.html"


def index(request):
    return render(request, "gcal/index.html", {
        'quoteText': "Everything",
        'quoteAttrib': '"This Moment is All there Is" --Rumi',
        'subheading1': "Build your routine, your way",
        'subtext1': ''' Find out where your spend your time, 
                    setgoals and check in on your progress 
                    with minimal effort--all in from within 
                    the calendar you already know & love: 
                    Google Calendar ''',
        'subheading2': "Show the muse you're serious",
        'subtext2': ''' You have to show up for your dreams; no 
                    one can do it for you but we can give 
                    you the tools to stay present '''
        })


def events_list(request):
    current_events_list = CalEvent.objects.order_by()
    context = {
        'current_events_list': current_events_list,
    }
    template = loader.get_template('gcal/events_list.html')
    return HttpResponse(template.render(context, request))
