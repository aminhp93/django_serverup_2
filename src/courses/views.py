import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
	)

from .forms import CourseForm
from .models import Course, Lecture
from videos.mixins import MemberRequiredMixin, StaffMemberRequiredMixin

# Create your views here.

class CourseCreateView(LoginRequiredMixin, CreateView):
	model = Course 
	form_class = CourseForm
	# success_url = "/"

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super().form_valid(form)

class LectureDetailView(MemberRequiredMixin, DetailView):
	def get_object(self):
		course_slug = self.kwargs.get("cslug")
		lecture_slug = self.kwargs.get("lslug")
		obj = get_object_or_404(Lecture, course__slug=course_slug, slug=lecture_slug)
		return obj

class CourseDetailView(StaffMemberRequiredMixin, DetailView):
	queryset = Course.objects.all()

	def get_object(self):
		slug = self.kwargs.get("slug")

		obj = Course.objects.filter(slug=slug)
		if obj.exists():
			return obj.first()
		raise Http404
		# try:
		# 	obj = Course.objects.get(slug=slug)
		# except Course.MultipleObjectsReturned:
		# 	qs = Course.objects.filter(slug=slug)
		# 	if qs.exists():
		# 		obj = qs.first()
		# except:
		# 	raise Http404
		# return obj

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
		print("saf")
		obj = form.save(commit=False)
		if not self.request.user.is_staff:
			obj.user = self.request.user
		obj.save()
		return super().form_valid(form)

	def get_object(self):
		print("88")
		slug = self.kwargs.get("slug")
				
		obj = Course.objects.filter(slug=slug)
		if obj.exists():
			return obj.first()
		raise Http404

class CourseDeleteView(DeleteView):
	queryset = Course.objects.all()
	success_url = "/courses/"

	def get_object(self):
		slug = self.kwargs.get("slug")
				
		obj = Course.objects.filter(slug=slug)
		if obj.exists():
			return obj.first()
		raise Http404