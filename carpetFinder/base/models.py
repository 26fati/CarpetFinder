from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='userProfile', null=True, blank=True, on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='profile_images', null=True, blank=True)