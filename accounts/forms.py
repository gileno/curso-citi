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
