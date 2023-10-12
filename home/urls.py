from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('read/', views.read, name='read'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    path('read/dm/', views.dm, name='dm'),
    path('read/dm/classification', views.clfn, name='clfn'),
    path('read/dm/classification/easy', views.clfn_easy, name='clfn_easy'),
  

    
]