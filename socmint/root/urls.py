from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/twitter/',views.twitter,name='twitter'),
    path('home/reddit/',views.reddit,name='reddit'),
]