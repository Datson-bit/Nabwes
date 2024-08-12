from django.urls import path

from .views import home, about, contact, gallery, blog, events, service, causes,team


urlpatterns = [
    path('', home, name='home'),
    path("blog/", blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('events', events, name='events'),
    path('gallery', gallery, name='gallery'),
    path('service', service, name='service'),
    path('causes', causes, name='causes'),
    path('team/', team, name='team')

]