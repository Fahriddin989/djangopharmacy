from django.urls import path
from .forms import LoginForm
from . import views

app_name = 'account'

urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

]