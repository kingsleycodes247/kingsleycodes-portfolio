from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .models import Blog, Project, Service
from .forms import ContactForm


def home(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    blogs = Blog.objects.order_by('-created_at')[:3]  # show latest blogs on homepage
    context = {
        'services': services,
        'projects': projects,
        'blogs': blogs,
        'calendly_link': 'https://calendly.com/kingsleycodes247/30min',
        'upwork_link': 'https://www.upwork.com/freelancers/~01217e81acabdbc9fa?mp_source=share',
    }
    return render(request, 'home.html', context)


def about(request):
    services = Service.objects.all()
    return render(request, "about.html", {"services": services})


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def contact(request):
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
                return redirect('contact_success')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f'Error sending email: {e}')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'calendly_link': 'https://calendly.com/kingsleycodes247/30min'
    })

def contact_success(request):
    return render(request, 'contact_success.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    other_services = Service.objects.exclude(id=service.id)
    return render(request, 'service_detail.html', {
        'service': service,
        'other_services': other_services
    })

def blog_list(request):
    blogs = Blog.objects.order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})
