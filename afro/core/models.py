from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class myresume(models.Model):
    file = models.FileField(upload_to='static/afro/uploads/')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, default='default')
    slug = models.SlugField(max_length=200, unique=True, default='default')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', default='admin')
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='afro/img', blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/afro/uploads/projects')

    def __str__(self):
        return self.name

class newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





