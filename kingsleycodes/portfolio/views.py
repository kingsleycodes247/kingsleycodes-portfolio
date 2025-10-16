from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .models import Blog, Service
from .forms import ContactForm


def home(request):
    services = Service.objects.all()[:6]
    blogs = Blog.objects.order_by('-created_at')[:3]  # show latest blogs on homepage
    context = {
        'services': services,
        'blogs': blogs,
        'calendly_link': 'https://calendly.com/kingsleycodes247/30min',
        'upwork_link': 'https://www.upwork.com/freelancers/~01217e81acabdbc9fa?mp_source=share',
    }
    return render(request, 'home.html', context)


def about(request):
    skills = [
        "Mobile Development",
        "Web Development",
        "DevOps & Cloud",
        "Blockchain",
        "AI & Automation",
        "UI/UX Design",
        "Digital Marketing",
        "Technical Writing",
    ]
    return render(request, "about.html", {"skills": skills})


def projects(request):
    projects = [
        {
            'title': 'Price Sentinel',
            'summary': 'Real-time crypto alert app (Django + Celery + Redis).',
            'image': 'projects/price-sentinel.png',
            'stack': ['Django', 'Celery', 'Redis', 'Tailwind']
        },
        {
            'title': 'Akpa Wallet',
            'summary': 'Mobile fintech wallet with secure transactions (Android + Spring Boot).',
            'image': 'projects/akpa-wallet.png',
            'stack': ['Android', 'Java', 'Spring Boot']
        },
    ]
    context = {'projects': projects, 'calendly_link': 'https://calendly.com/kingsleycodes247/30min'}
    return render(request, 'projects.html', context)


def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Portfolio message from {name}'
            full_message = f"From: {name} <{email}>\n\n{message}"
            try:
                send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])
                success = True
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f'Error sending email: {e}')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form,
        'success': success,
        'calendly_link': 'https://calendly.com/kingsleycodes247/30min'
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def blog_list(request):
    blogs = Blog.objects.order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})
