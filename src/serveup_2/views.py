from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

def home(request):
	# return HttpResponse("hllo")
	return render(request, "home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("hello")


