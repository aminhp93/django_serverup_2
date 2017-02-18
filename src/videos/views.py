import random
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
	)

from .models import Video
# Create your views here.

class VideoCreateView(CreateView):
	queryset = Video.objects.all()

class VideoDetailView(DetailView):
	queryset = Video.objects.all()

	def get_object(self):
		abc = self.kwargs.get("slug")
		print(abc)
		return get_object_or_404(Video, slug=abc)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		print(context)
		return context

class VideoListView(ListView):
	queryset = Video.objects.all()

	# def get_queryset(self):
		# return Video.objects.filter(title__icontains="em")#.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["random_number"] = random.randint(0,10)
		print(context)
		return context

class VideoUpdateView(UpdateView):
	queryset = Video.objects.all()

class VideoDeleteView(DeleteView):
	queryset = Video.objects.all()
