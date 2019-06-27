from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery')
    #path('register/',UserCreationView.as_view(template_name='users/users_form.html'),name='user-create'),

]
