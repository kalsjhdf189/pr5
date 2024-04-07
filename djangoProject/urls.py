from django.contrib import admin
from django.urls import path
from PR3 import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('news', views.news),
    path('review', views.review),
]
