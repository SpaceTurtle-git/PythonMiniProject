from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})
