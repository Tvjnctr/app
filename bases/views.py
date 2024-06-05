from django.shortcuts import render

from django.views import generic

# Todas las clases son en Mayusculas
class Home(generic.TemplateView):
    template_name = 'bases/home.html'

