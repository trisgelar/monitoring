from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
	template_name = 'pages/home.html'