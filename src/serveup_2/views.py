import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
	def get(self, request, *args, **kwargs):
		context = {
			"name": "Minh",
			"random_number": random.randint(0, 500)
		}
		return render(request, "home.html", context)


