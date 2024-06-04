from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('twitter/',views.twitter,name='twitter'),
    path('reddit/',views.reddit,name='reddit'),
    path('telegram/',views.telegram,name='telegram'),
    path('instagram/',views.instagram,name='instagram'),
    path('reddit-api/', views.reddit_api_view, name='reddit_api_view'),
]