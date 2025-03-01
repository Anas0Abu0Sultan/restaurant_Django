from django import forms
from .models import Drinks, Salads, Meals, Sandwiches, Grills, Sweets

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'})
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control'})
    )


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = ['name', 'price', 'image', 'description', 'type_of_drink', 'small_price', 'medium_price', 'large_price']

class SaladForm(forms.ModelForm):
    class Meta:
        model = Salads
        fields = ['name', 'price', 'image', 'description', 'small_price', 'medium_price', 'large_price']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ['name', 'price', 'image', 'description']

class SandwichForm(forms.ModelForm):
    class Meta:
        model = Sandwiches
        fields = ['name', 'price', 'image', 'description']

class GrillForm(forms.ModelForm):
    class Meta:
        model = Grills
        fields = ['name', 'price', 'image', 'description']

class SweetForm(forms.ModelForm):
    class Meta:
        model = Sweets
        fields = ['name', 'price', 'image', 'description']