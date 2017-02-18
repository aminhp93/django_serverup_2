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

from .froms import CourseForm
from .models import Course
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin

# Create your views here.

class CourseCreateView(LoginRequiredMixin, CreateView):
	model = Course 
	form_class = CourseForm
	# success_url = "/"

	def form_valid(self, form):
		print("24", form)
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super().form_valid(form)

class CourseDetailView(StaffMemberRequiredMixin, DetailView):
	queryset = Course.objects.all()

	def get_object(self):
		abc = self.kwargs.get("slug")
		return get_object_or_404(Course, slug=abc)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		return context

class CourseListView(ListView):

	def get_queryset(self):
		request = self.request
		qs = Course.objects.all()
		query = request.GET.get('q')
		if query:
			qs = qs.filter(title__icontains=query)
		return qs#filter(title__icontains="em")#.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["random_number"] = random.randint(0,10)
		return context

class CourseUpdateView(UpdateView):
	queryset = Course.objects.all()
	form_class = CourseForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		if not self.request.user.is_staff:
			obj.user = self.request.user
		obj.save()
		return super().form_valid(form)

class CourseDeleteView(DeleteView):
	queryset = Course.objects.all()
	success_url = "/courses/"