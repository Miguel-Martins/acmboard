from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(max_length=30, label='First name', required=True)
    last_name = forms.CharField(max_length=30, label='Last name', required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.help_text = ''
            field.label=''


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    email=forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.help_text = ''
            field.label=''

    class Meta:
        model = User
        fields = ['email', 'password']