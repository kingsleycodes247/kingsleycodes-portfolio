from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('projects/', views.projects, name='projects'),
path('contact/', views.contact, name='contact'),
path('services/', views.services, name='services'),
path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
path('blog/', views.blog_list, name='blog_list'),
]