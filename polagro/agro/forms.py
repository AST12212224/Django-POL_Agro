from django import forms
from django.forms import ModelForm
from .models import product,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductCreate(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name","last_name","password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

