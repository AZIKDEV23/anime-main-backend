from django.shortcuts import render

# Create your views here.

def home(req):
    template_name = 'pages/home.html'
    return render(req, template_name)

def anime_details(req):
    template_name = 'pages/anime_details.html'
    return render(req, template_name)

def anime_watching(req):
    template_name = 'pages/anime-watching.html'
    return render(req, template_name)

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