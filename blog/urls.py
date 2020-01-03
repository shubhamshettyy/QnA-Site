from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('blog/',views.about, name='blog-about')
    #path('blog/',include('blog.urls'))

]