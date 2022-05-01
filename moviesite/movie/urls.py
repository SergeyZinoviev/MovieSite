from django.urls import path

from.views import *

urlpatterns = [ 
    path('', Home.as_view(), name='home'),
    path('news/', news, name='news'),
    path('comsoon/', comsoon, name='comsoon'),
    path('<str:slug>/', GetPost.as_view(), name='post'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('search/', Search.as_view(), name='search'),
]