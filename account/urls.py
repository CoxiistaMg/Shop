from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout', views.logoutQ, name='logout'),
    path('create_login', views.createlogin, name='create'),
    path('emailVerification/<uidb64>/<token>', views.activate, name='emailActivate'),
    path('emailVerification/<uidb64>/<token>', views.activate, name='emailActivate') 
]
