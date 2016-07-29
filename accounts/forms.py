# coding=utf-8

from django import forms

from .models import User


class RegisterUserForm(forms.ModelForm):

    def save(self):
        super(RegisterUserForm, self).save(commit=False)
        self.instance.set_password(self.cleaned_data['password'])
        self.instance.save()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email']


class PasswordChangeForm(forms.Form):

    old_password = forms.CharField(label='Senha antiga', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nova Senha', widget=forms.PasswordInput)
    new_password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput
    )

    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password', '')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Senha incorreta')
        return old_password

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1', '')
        new_password2 = self.cleaned_data.get('new_password2', '')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('A confirmação de senha não confere')
        return new_password2
