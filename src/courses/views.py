import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
		RedirectView,
	)

from .forms import CourseForm
from .models import Course, Lecture, MyCourse

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

class CoursePurchaseView(LoginRequiredMixin, RedirectView):
	permanent = False    

	def get_redirect_url(self, slug=None):
		qs = Course.objects.filter(slug=slug).owned(self.request.user)
		if qs.exists():
			user = self.request.user

			if user.is_authenticated():
				my_course = user.mycourse
				# if transaction successful:
				my_course.courses.add(qs.first())
			return qs.first().get_absolute_url()
		return "/courses/"

class CourseDetailView(LoginRequiredMixin, DetailView):
	queryset = Course.objects.all()

	def get_object(self):
		slug = self.kwargs.get("slug")

		qs = Course.objects.filter(slug=slug).owned(self.request.user)
		if qs.exists():
			return qs.first()
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
		user = self.request.user
		if query:
			qs = qs.filter(title__icontains=query)
		if user.is_authenticated():
			# qs = qs.prefetch_related(
			# 		Prefetch("owned",
			# 			queryset=MyCourse.objects.filter(user=user),
			# 			to_attr="is_owner",
			# 		)
			# 	)
			qs = qs.owned(user)
		return qs#filter(title__icontains="em")#.filter(user=self.request.user)

class CourseUpdateView(UpdateView):
	queryset = Course.objects.all()
	form_class = CourseForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		if not self.request.user.is_staff:
			obj.user = self.request.user
		obj.save()
		return super().form_valid(form)

	def get_object(self):
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