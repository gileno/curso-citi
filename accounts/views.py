# coding=utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm


@login_required
def index(request):
    return render(request, 'accounts/index.html')


def register(request):
    form = RegisterUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
