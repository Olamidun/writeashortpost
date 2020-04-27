from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20,
                               help_text='<b>Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.</b>',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control mb-2',
                                       'placeholder': 'Enter username',
                                    }))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Enter your email address'
        }
    ))
    password1 = forms.CharField(help_text=
                                '''<b>Your password can’t be too similar to your other personal information.
                                   Your password must contain at least 8 characters.
                                   Your password can’t be a commonly used password.
                                   Your password can’t be entirely numeric.</b>''',

                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control mb-2',
                                        'placeholder': 'Enter your password'
                                    }))

    password2 = forms.CharField(
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control mb-2',
                                        'placeholder': 'Enter your password again for confirmation'
                                    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=20,
                               help_text='<b>Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.</b>',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control mb-2',
                                       'placeholder': 'Enter username',

}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Enter your email address'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = CloudinaryFileField(
        options={
            # 'crop': 'fill',
            # 'width': 50,
            # 'height': 50,
            'folder': 'profile_pics'
        }
    )

    class Meta:
        model = Profile
        fields = ['image']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control mb-2',
                                       'placeholder': 'Enter username',

}))
    password = forms.CharField(
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control mb-2',
                                        'placeholder': 'Enter your password!'
                                    }))


