from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from videos.models import Video
from .fields import PositionField

# from .utils import create_slug

# Create your models here.
class Course(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL)
	title 		    = models.CharField(max_length=120)
	slug 			= models.SlugField(blank=True) # unique=True
	description 	= models.TextField()
	price 			= models.DecimalField(decimal_places=2, max_digits=100)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("courses:detail", kwargs={"slug": self.slug})

# limit_choices_to={"lecture__isnull": True}
class Lecture(models.Model):
	course 			= models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
	video 			= models.ForeignKey(Video, on_delete=models.SET_NULL, null=True) 
	title 		    = models.CharField(max_length=120)
	order 			= PositionField(collection="course")
	slug 			= models.SlugField(blank=True) # unique=True
	description 	= models.TextField(blank=True)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.title

	class Meta:
		unique_together = (('slug', 'course'))
		ordering = ['-order', '-title']

	def get_absolute_url(self):
		return reverse("courses:lecture-detail", kwargs={"cslug": self.course.slug, "lslug":self.slug})

def pre_save_video_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance)

pre_save.connect(pre_save_video_receiver, sender=Course)
pre_save.connect(pre_save_video_receiver, sender=Lecture)
