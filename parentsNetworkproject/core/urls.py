from django.contrib import admin
from django.urls import path , include
from .views import *
from . import views
urlpatterns = [
 path('',login_page,name='login'),
 path('signup/' , SignupView.as_view(),name='signup'),
 path('logout/',logout_user,name='logout'),
 path('profile/',profile,name='profile'),
 path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),


 path('addParent/', views.addParent, name='addParent'),
 path('deleteParent/<str:pk>', views.deleteParent, name='deleteParent'),

 path('toDoList/', views.toDoList, name='toDoList'),
 path('add_task/', views.addTask, name='add_task'),
 path('delete_task/<str:pk>', views.deleteTask, name='delete_task'),
 path('show_parent_schedule/<int:pk>', show_parent_schedule, name="show_parent_schedule"),
 path('all_schedule/', all_schedule, name="all_schedule"),
 path('manage_parent_schedule/<int:pk>/', manage_parent_schedule, name="manage_parent_schedule"),
 path('edit_schedule/<int:pk>/', edit_schedule, name="edit_schedule"),
 path('contact_parent/', contact_parent, name="contact_parent"),
 path('contact_admin/', contact_admin, name="contact_admin"),

]
