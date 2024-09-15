from django.urls import path

from .views import home, about, contact, gallery, blog, events, service, causes, donation, error_404, \
    members, team_sec, team_spc

urlpatterns = [
    path('', home, name='home'),
    path("blog/", blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('service/', service, name='service'),
    path('causes/', causes, name='causes'),
    path('team_sec/', team_sec, name='team_sec'),
    path('team_spc/', team_spc, name='team_spc'),
    path('donation/', donation, name='donation'),
    path('error_404/', error_404, name='error_404'),
    path('members/', members, name='members'),
]