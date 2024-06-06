from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('twitter/',views.twitter,name='twitter'),
    path('reddit/',views.reddit,name='reddit'),
    path('telegram/',views.telegram,name='telegram'),
    path('instagram/',views.instagram,name='instagram'),
]