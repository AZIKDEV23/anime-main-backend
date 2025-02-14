from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('anime_details/', anime_details, name='anime_details'),
    path('anime_watching/', anime_watching, name='anime_watching'),
    path('blog/', blog, name='blog'),
    path('blog_details/', blog_details, name='blog-details'),
    path('categories/', categories, name='categories'),
    path('login/', login, name='login'),
    path('signup', signup, name='signup')
]