from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import json


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimestampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Blog(TimestampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default="Kingsley Ofoma")

    try:
        content = RichTextField()
    except ImportError:
        content = models.TextField()

    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Service(TimestampedModel):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    short = models.CharField(max_length=255, default='brief description of the service')
    long = models.TextField(default='description of the service')
    icon = models.CharField(max_length=100, help_text="Use a Lucide icon name or FontAwesome icon class")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    faqs = models.JSONField(default=list, blank=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContactMessage(TimestampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
