from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, DetailView

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
    template_name = 'pages/login.html'
    return render(req, template_name)

def signup(req):
    template_name = 'pages/signup.html'
    return render(req, template_name)