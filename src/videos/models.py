from django.db import models

# Create your models here.
class Video(models.Model):
	embed_code 	= models.TextField()
	title 		= models.CharField(max_length=120)
	slug 		= models.SlugField(blank=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title