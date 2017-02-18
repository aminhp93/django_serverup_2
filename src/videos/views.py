import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
	)

from .models import Video
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .forms import VideoForm

# Create your views here.

class VideoCreateView(LoginRequiredMixin, CreateView):
	model = Video 
	form_class = VideoForm
	# success_url = "/"

class VideoDetailView(StaffMemberRequiredMixin, DetailView):
	queryset = Video.objects.all()

	def get_object(self):
		abc = self.kwargs.get("slug")
		return get_object_or_404(Video, slug=abc)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		return context

class VideoListView(ListView):

	def get_queryset(self):
		request = self.request
		qs = Video.objects.all()
		query = request.GET.get('q')
		if query:
			qs = qs.filter(title__icontains=query)
		return qs#filter(title__icontains="em")#.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["random_number"] = random.randint(0,10)
		return context

class VideoUpdateView(UpdateView):
	queryset = Video.objects.all()

class VideoDeleteView(DeleteView):
	queryset = Video.objects.all()
