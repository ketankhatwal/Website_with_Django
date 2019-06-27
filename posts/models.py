from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
import os

class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	image=models.ImageField(default='content_pics\\default_post.jpg',upload_to='content_pics')
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def save(self):
		super().save()

	def get_absolute_url(self):
		return reverse('home')

#@receiver(post_delete, sender=Post)
#def auto_delete_file_on_delete(sender, instance, **kwargs):
#
#    Deletes file from filesystem
#    when corresponding `MediaFile` object is deleted.
#
#    if instance.image:
#    	if os.path.isfile(instance.image.path):
#    		print(instance.image.path)
#    		if instance.image.path!=os.getcwd()+'\\media\\content_pics\\default_post.jpg':
#    			os.remove(instance.image.path)
    		
    			
				


	