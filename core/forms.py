# coding=utf-8

from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    # def clean(self):
    #     # raise forms.ValidationError('Erro Geral')
    #     return self.cleaned_data

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'fulano':
            raise forms.ValidationError('Este não pode ser seu nome')
        return name
