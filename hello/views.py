from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .tasks import my_task
import os
import requests

# Create your views here.
def index(request):
    #times = int(os.environ.get('TIMES',3))
    #return HttpResponse('Hello - World - whats up?? ' * times)
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def progress_view(request):
    result = my_task.delay(10)
    return render(request, 'display_progress.html', context={'task_id': result.task_id})
