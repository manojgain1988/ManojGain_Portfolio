
from django.urls import path
from IndexApp import views


urlpatterns = [
    path('', views.Index , name='index'),
    path('about/', views.Abouts , name='about'),
    path('services/', views.Services , name='services'),
    path('team/', views.Team , name='team'),
    path('portfolio/', views.Portfolios , name='portfolio'),
    path('profile/', views.Profile , name='profile'),
    path('contact/', views.Contact , name='contact'),
    
    
    path('login/', views.AuthLogin , name='login'),
    path('register/', views.AuthRegister , name='register'),
    path('forgot/', views.Forgotpassword , name='forgot'),
    path('logout/', views.UserLogout , name='logout'),
   
]