from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User, Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'email': 'email',
            'password1': 'Введите пароль',
            'password2': 'Повторите пароль'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = u'Your name'
        self.fields['username'].widget.attrs['placeholder'] = u'Username'
        self.fields['email'].widget.attrs['placeholder'] = u'Email'
        self.fields['password1'].widget.attrs['placeholder'] = u'Password'
        self.fields['password2'].widget.attrs['placeholder'] = u'Repeat password'
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'profile_image']
        labels = {
            'name': 'Имя',
            'profile_image': 'Аватарка',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

