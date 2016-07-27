# coding=utf-8

from django.shortcuts import render, redirect

from .forms import RegisterUserForm


def register(request):
    form = RegisterUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
