from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Gallery,Subscriber, Blog, Event, Comment, Registration, EventPass, Executives, Parliamentary
from .forms import CommentForm, RegistrationForm, SubscriberForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
import random
import string

import qrcode
import base64
from io import BytesIO
from PIL import Image

def home(request):
    blog = Blog.objects.all().order_by('-id')[:8]
    carousel = Blog.objects.all().order_by('-id')[:3]
    event = Event.objects.all().order_by('-id')[:5]
    gallery = Gallery.objects.all().order_by('-id')[:4]

    return render(request, 'index.html', {'blogs': blog, 'carousel': carousel, 'gallery': gallery, 'events':event})

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email address'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 12)
    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'blog':paginated_posts})

def blog_view(request, pk):
    global comment_form
    blog = get_object_or_404(Blog, pk=pk)
    # view count
    if not hasattr(blog, 'view_count'):
        blog = Blog.objects.get(pk=pk)
    
    blog.view_count += 1
    blog.save()

    # comments
    comments = Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()

    else:
        comment_form = CommentForm()
    return render(request, 'blog_view.html', {'blogs':blog, 'comments': comments, 'form':comment_form})


def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events':events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id= event_id)
    sponsors = event.sponsors.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            # if event.registrations.count() < event.capacity:
            registration.save()
            pass_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k= 8))
            EventPass.objects.create(registration=registration, pass_code=pass_code)
            return redirect('registration_success', registration_id= registration.id)
            # else:
            #     return render(request, 'events_full.html', {'event':event})
    else:
        form = RegistrationForm()
        return render(request, 'event_d.html', {'event':event, 'form':form, 'sponsors':sponsors, 'event_date': event.date.strftime('%Y-%m-%dT%H:%M:%S'),})


def registration_success(request, registration_id):
    registration = get_object_or_404(Registration, id= registration_id)
   
    # Generate QR code

    # Generate QR code data
    qr_data = f"Event: {registration.event.title}\nName: {registration.full_name}\nPass Code: {registration.event_pass.pass_code}"

    # Create QR code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert QR code to base64
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'registration_success.html', {'registration': registration, 'qr_code': qr_base64})


def gallery(request):
    galleries= Gallery.objects.all()
    paginator = Paginator(galleries, 4)
    page = request.GET.get('page')
    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)
    return render(request, 'gallery.html', {'galleries': paginated_posts})

def test(request):
    return render(request, 'gallery_test.html')

def service(request):
    return render(request, 'service.html')


def causes(request):
    return render(request, 'causes.html')


def executives(request):
    executives = Executives.objects.all()
    return render(request, 'team_sec.html', {'executives':executives})


def parliamentary(request):
    parliamentary = Parliamentary.objects.all()
    return render(request, 'team_spc.html', {'parliamentary': parliamentary})


def donation(request):
    return render(request, 'donation.html')

def custom_404_test(request):
    return HttpResponseNotFound(render(request, '404.html'))

def members(request):
    return render(request, 'members.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  'Thank you for subscribing to our newsletter!')
            return redirect('subscribe')
        else:
            messages.error(request, 'Invalid email. Please Try again')
    else:
        form = SubscriberForm()
    return render(request, 'base.html', {'form': form})