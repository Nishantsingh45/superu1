from django.db import models

# Create your models here.
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
   # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    # Add any additional fields you require for the user profilepython manage.py makemigrations