from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('twitter/',views.twitter,name='twitter'),
    path('reddit/',views.reddit,name='reddit'),
    path('reddit/',views.reddit,name='telegram'),
    path('reddit/',views.reddit,name='instagram'),
]