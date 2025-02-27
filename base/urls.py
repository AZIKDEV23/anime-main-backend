from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('anime_details/<slug:slug>/', AnimeDetailPageView.as_view(), name='anime_details'),
    path('anime_watching/<slug:slug>/', AnimeWatchingPageView.as_view(), name='anime_watching'),
    path('blog/', blog, name='blog'),
    path('blog_details/', blog_details, name='blog-details'),
    path('categories/', categories, name='categories'),
    path('login/', login, name='login'),
    path('signup', signup, name='signup')
]