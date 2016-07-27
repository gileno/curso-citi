# coding=utf-8

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm, EditUserForm


@login_required
def index(request):
    return render(request, 'accounts/index.html')


@login_required
def edit(request):
    form = EditUserForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Dados salvos com sucesso')
        return redirect('accounts:index')
    context = {
        'form': form
    }
    return render(request, 'accounts/edit.html', context)


def register(request):
    form = RegisterUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
