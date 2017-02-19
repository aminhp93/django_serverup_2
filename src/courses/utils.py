import string
import random

from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.text import slugify


def unique_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
	print(string.ascii_lowercase, string.digits)
	return "".join(random.choice(chars) for _ in range(size))

def create_slug(instance, new_slug=None):
	if not new_slug:
		slug = slugify(instance.title)
	else:
		slug = new_slug
	Klass = instance.__class__
	print(Klass)
	qs = Klass.objects.filter(slug=slug).order_by("-id")
	if qs.exists():
		# return slug + "-1"
		string_unique = unique_string_generator()
		newly_created_slug = slug + "-{id}".format(id=string_unique)
		return create_slug(instance,new_slug=newly_created_slug)
	return slug

def make_display_price(price):
	dollars = round(price, 2)
	return "${}{}".format(intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])