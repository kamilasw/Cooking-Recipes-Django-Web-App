from django.urls import path
from .views import signup

urlpatterns = [
    path('registration/signup/', signup, name='signup'),
]