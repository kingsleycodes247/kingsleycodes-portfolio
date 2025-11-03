from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('projects/', views.projects, name='projects'),
path('contact/', views.contact, name='contact'),
path('contact/success/', views.contact_success, name='contact_success'),
path('services/', views.services, name='services'),
path('services/<slug:slug>/', views.service_detail, name='service_detail'),
path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
path('blog/', views.blog_list, name='blog_list'),
]