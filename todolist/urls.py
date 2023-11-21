from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('',views.home),
   path('contact',views.contact),
   path('about',views.about),
   path('create',views.create),
   path('mark/<pk>',views.mark),
   path('edit/<pk>',views.edit),
   path('update/<pk>',views.update),
   path('delete/<pk>',views.delete),
 
]
