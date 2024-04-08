from django.contrib import admin
from django.urls import path , include
from .views import *
from . import views
urlpatterns = [
 path('',login_page,name='login'),
 path('signup/' , SignupView.as_view(),name='signup'),
 path('logout/',logout_user,name='logout'),
 path('profile/',profile,name='profile'),
 path('show_parent_schedule/<int:pk>', show_parent_schedule, name="show_parent_schedule"),
 path('all_schedule/', all_schedule, name="all_schedule"),
 path('manage_parent_schedule/<int:pk>/', manage_parent_schedule, name="manage_parent_schedule"),
]
