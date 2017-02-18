from django import forms

from .models import Course

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			'title',
			'description',
			'slug',
			'price',
		]

	def clean_slug(self):
		slug = self.cleaned_data.get("slug")
		qs = Course.objects.filter(slug=slug)
		if qs.exists():
			raise forms.ValidationError("slug does exist")
		return slug

