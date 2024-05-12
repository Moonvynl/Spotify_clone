from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth_system/login.html' , extra_context={'next': reverse_lazy('spotify:home')}), name='login' ),
    path('register/', RegisterView.as_view(template_name='auth_system/register.html'), name='register'),
]

app_name = 'auth_system'