from django.contrib import admin
from testapp import views
from django.urls import path
urlpatterns = [
    path('first/', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
    ]
