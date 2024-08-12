from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def events(request):
    return render(request, 'events.html')


def gallery(request):
    return render(request, 'meet_us.html')


def service(request):
    return render(request, 'service.html')


def causes(request):
    return render(request, 'causes.html')


def team(request):
    return render(request, 'team.html')

