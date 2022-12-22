from . import views
from django.contrib import messages
from django.urls import path
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from .forms import NewsLetterForm
from django.views.generic import DetailView
from django.views.generic import FormView
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.



def home(request):
    context = {}
    return render(request,"afro/home.html", context)


def about(request):
    context = {}
    return render (request, 'afro/about.html', context)


def testimonials(request):
    context = {}
    return render(request, 'afro/testimonials.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'afro/contact.html', {'form': form})


def project(request):
    projects = Project.objects.all()
    return render(request, 'afro/projects.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'afro/project_detail.html', {'project': project})

def resume(request):
    context = {}
    return render(request, 'afro/resume.html', context)

class myresumeview(DetailView):
    model = myresume

def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            # Save the email address to your database
            email = form.cleaned_data['email']
            form.save()
            # Redirect to a success page
            return redirect('home')
    else:
        form = NewsLetterForm()
    return render(request, 'afro/newsletter.html', {'form': form})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'afro/blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'afro/post_detail.html'
