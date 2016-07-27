import random

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = '[DjangoEcommerce] %s entrou em contato' % name
            body = 'E-mail: %s\n%s' % (email, message)
            send_mail(subject, body, 'admin@admin.com', ['contato@admin.com'])
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
