from django.urls import path

from .views import home, about, contact, gallery, blog, events, service, event_detail, registration_success, causes, donation, error_404, test,members, executives,  blog_view, parliamentary

urlpatterns = [
    path('', home, name='home'),
    path('test/', test),
    path("blog/", blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('service/', service, name='service'),
    path('causes/', causes, name='causes'),
    path('executives/', executives, name='executives'),
    path('parliamentary/', parliamentary, name='team_spc'),
    path('donation/', donation, name='donation'),
    path('error_404/', error_404, name='error_404'),
    path('members/', members, name='members'),
    path('blog/<int:pk>/', blog_view, name="view"),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('registration-success/<int:registration_id>/', registration_success, name='registration_success')
]