from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('register', views.RegisterView.as_view(), name='register-user'),
    path('login', views.LoginView.as_view(), name='login-user')
])