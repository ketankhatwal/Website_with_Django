from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic=models.ImageField(default='profile_pics\\default_user.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} profile'

#	def save(self, *args, **kwargs):
#		super().save(*args, **kwargs)

