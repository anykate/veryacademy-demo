from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..accounts.forms import UpdateUserForm
from .forms import ProfileUserForm


# Create your views here.
@login_required
def profile(request):
    u_form = UpdateUserForm(request.POST or None, instance=request.user)
    p_form = ProfileUserForm(
        request.POST or None,
        instance=request.user.profiles
    )

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f'Profile updated successfully!')
        return redirect('profiles:profile')

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profiles/profile.html', context)
