from django.urls import path
from django.contrib.auth.views import login_required, logout_then_login
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
]
