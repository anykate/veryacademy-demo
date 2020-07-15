from django.shortcuts import render
from django.views.generic import View
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# @login_required
# def home(request):
#     return render(request, 'core/index.html', {})


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/index.html', {})


class AboutView(View):
    def get(self, request):
        return render(request, 'core/about.html', {})


class ContactView(View):
    def get(self, request):
        return render(request, 'core/contact.html', {})
