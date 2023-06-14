from django.urls import path
from .api import create_or_update_profile

urlpatterns = [
    path('profiles/', create_or_update_profile, name='create_or_update_profile'),
    
]
