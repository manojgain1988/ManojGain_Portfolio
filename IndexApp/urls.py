
from django.urls import path
from IndexApp import views


urlpatterns = [
    path('', views.Index , name='index'),
    path('about/', views.About , name='about'),
    path('services/', views.Services , name='services'),
    path('team/', views.Team , name='team'),
    path('portfolio/', views.Portfolio , name='portfolio'),
    path('testimonial/', views.Testimonial , name='testimonial'),
    path('contact/', views.Contact , name='contact'),
    
    
    path('login/', views.Login , name='login'),
    path('register/', views.Register , name='register'),
   
]