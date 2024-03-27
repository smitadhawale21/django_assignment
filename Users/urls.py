
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration),
    path('verification/', views.verification),
    path('login/', views.login),
    path('forgot_password/', views.forgot_password),
    path('reset_password/', views.reset_password),
]
