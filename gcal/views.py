from django.http import HttpResponse
from django.template import loader
#from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import CalEvent


def contact_view(request):
    return render(request, "gcal/contact.html", {
        'title': "Contact",
        'contactBttnClass': "active",
        'quoteText': "Contact",
        'quoteAttrib': "",
        'subheading1': "Google Voice",
        'subtext1': "503 468 7021",
        'subheading2': "",
        'subtext2': ""
        })


def about_view(request):
    return render(request, "gcal/about.html", {
        'title': "About",
        'aboutBttnClass': "active",
        'quoteText': "About",
        'quoteAttrib': "",
        'subheading1': "Read-only parsing of your calendar data",
        'subtext1': """Timing.is will not store your data. It will
                    produce summary charts describing the amount
                    and percent of of total for all unique events
                    by calendar or time spent in various
                    categories determined by a \'tag\'of your
                    choosing, which can be any word or phrase
                    that you want to use. Activity domains, such
                    as physical, social, spiritual or mental;
                    categorical markers, like professional,
                    personal or communal.""",
        'subheading2': "Source Code Available on Github",
        'subtext2': """https://github.com/eayoungs/Timing.is\n
                    The underlying functionality is provided by
                    by the GeePal library:\n
                    https://pypi.python.org/pypi/geepal"""
        })


def index(request):
    return render(request, "gcal/index.html", {
        'title': "Home",
        'indexBttnClass': "active",
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

def auth_user(request):
    return render(request, "gcal/auth_user.html", {
        'title': "Login"
        })


def events_list(request):
    current_events_list = CalEvent.objects.order_by()
    context = {
        'current_events_list': current_events_list,
    }
    template = loader.get_template('gcal/events_list.html')
    return HttpResponse(template.render(context, request))
