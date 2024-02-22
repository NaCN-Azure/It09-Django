# application/forms/form.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from application.models.user_model import User
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'user_name', 'phone', 'city', 'type')
        field_order = ['email', 'user_name', 'phone', 'city', 'password1', 'password2', 'type']
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomLoginForm(AuthenticationForm):
    pass


