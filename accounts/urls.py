from django.urls import path, include
from . import views

urlpatterns = [
    path('sign-up', views.sign_up, name='sign_up'),
    # path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
]
