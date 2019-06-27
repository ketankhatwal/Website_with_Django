from django.contrib import admin
from django.urls import path,include
from .views import UserCreationView

urlpatterns = [
    path('register/',UserCreationView.as_view(),name='user-create'),

]
