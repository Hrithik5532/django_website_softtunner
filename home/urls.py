from django.contrib import admin
from django.urls import path
from  home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('index.html',views.index, name='home'),
    path('about.html',views.about, name='about'),
    path('contact.html',views.contact, name='contact.html'),
    path('contact',views.contact, name='contact'),

    path('blog.html',views.blog, name='blog'),
    path('blog-signal.html',views.index, name='blog-signal'),
    path('services.html', views.services, name='service'),
    path("blog-singal", views.blog_singal)
]