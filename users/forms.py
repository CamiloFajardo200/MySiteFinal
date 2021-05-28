from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


CATEGORIES = (
    ('', 'Choose...'),
    ('PC', 'PC'),
    ('PS4', 'PlayStation4'),
    ('PS5', 'PlayStation5'),
    ('XBO', 'XBOXONE'),
    ('XBSX', 'XBOX Series X'),
    ('SWITCH', 'Nintendo Switch'),
    ('XBSS', 'XBOX Series S')
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    category = forms.ChoiceField(choices=CATEGORIES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
