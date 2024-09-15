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
    return render(request, 'gallery.html')


def service(request):
    return render(request, 'service.html')


def causes(request):
    return render(request, 'causes.html')


def team_sec(request):
    return render(request, 'team_sec.html')


def team_spc(request):
    return render(request, 'team_spc.html')


def donation(request):
    return render(request, 'donation.html')


def error_404(request):
    return render(request, '404.html')


def members(request):
    return render(request, 'members.html')

