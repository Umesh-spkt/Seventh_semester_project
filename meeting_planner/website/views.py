from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task


def welcome(request):
    return render(request, "website/welcome.html",
                  {"tasks": Task.objects.all()})


def about(request):
    return render(request, 'website/about.html')


