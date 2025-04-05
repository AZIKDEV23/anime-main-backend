from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from .forms import *
from .models import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView

# Create your views here.

class HomePageView(ListView):
    model = Anime
    template_name = 'pages/home.html'
    ordering = ['-created_at']
    context_object_name = 'animes'

class AnimeDetailPageView(DetailView):
    model = Anime
    template_name = 'pages/anime_details.html'
    context_object_name = 'anime'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_animes"] = Anime.objects.all()
        return context
class AnimeWatchingPageView(DetailView):
    model = Anime
    template_name = 'pages/anime-watching.html'
    context_object_name = 'anime'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def blog(req):
    template_name = 'pages/blog.html'
    return render(req, template_name)

def blog_details(req):
    template_name = 'pages/blog-details.html'
    return render(req, template_name)

def categories(req):
    template_name = 'pages/categories.html'
    return render(req, template_name)

def login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(req, 'pages/login.html', {'form': form})

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def signup(req):
    if req.method == 'POST':
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(req, 'pages/signup.html', {'form': form})

    context = {'form': form}

    template_name = 'pages/signup.html'
    return render(req, template_name, context)

def logout(req):
    logout(req)
    return redirect('home')

@login_required
def home_view(req):
    template_name = 'pages/home.html'
    return render(req, template_name)
