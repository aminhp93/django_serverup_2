from django.shortcuts import render
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
		RedirectView,
	)

from .models import Category
# Create your views here.

class CategoryListView(ListView):
	queryset = Category.objects.all().order_by('title')

class CategoryDetailView(DetailView):
	queryset = Category.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		# obj = self.get_object()
		obj = context.get("object")
		print(context, obj)
		user = self.request.user
		qs1 = obj.primary_category.all()
		qs2 = obj.secondary_category.all()
		if user.is_authenticated():
			qs1 = qs1.owned(self.request.user)
			qs2 = qs2.owned(self.request.user)
		qs = (qs1 | qs2).distinct()
		context['courses'] = qs
		return context