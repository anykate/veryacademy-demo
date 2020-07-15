from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import AddUserForm, LoginUserForm


# Create your views here.
class RegisterUserView(View):
    template_name = 'accounts/register.html'
    form_class = AddUserForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully !!')
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class LoginUserView(View):
    template_name = 'registration/login.html'
    form_class = LoginUserForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if form.is_valid():
            login(request, user)
            messages.success(
                request, f'Welcome, {user.username.capitalize()} !!')
            return redirect('core:home_cbv')
        return render(request, self.template_name, {'form': form})
