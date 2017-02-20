from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from courses.utils import create_slug
from courses.fields import PositionField
# Create your models here.

class CategoryQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

class CategoryManager(models.Manager):
	def get_queryset(self):
		return CategoryQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().all().active()

class Category(models.Model):
	title 		    = models.CharField(max_length=120)
	slug 			= models.SlugField(blank=True) # unique=True
	description 	= models.TextField()
	order 			= PositionField(blank=True)
	active 			= models.BooleanField(default=True)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True) 

	objects = CategoryManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("categories:detail", kwargs={"slug": self.slug})

def pre_save_category_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_category_receiver, sender=Category)