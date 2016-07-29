# coding=utf-8

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.contrib.auth import update_session_auth_hash

from .forms import RegisterUserForm, EditUserForm, PasswordChangeForm


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


class PasswordChangeView(FormView):

    template_name = 'accounts/password_change.html'
    form_class = PasswordChangeForm

    def get_success_url(self):
        messages.success(self.request, 'Senha alterada com sucesso')
        return reverse('accounts:index')

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.request.user.set_password(form.cleaned_data['new_password1'])
        self.request.user.save()
        update_session_auth_hash(self.request, self.request.user)
        return super(PasswordChangeView, self).form_valid(form)
