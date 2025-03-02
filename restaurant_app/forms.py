from django import forms
from .models import Drinks, Salads, Meals, Sandwiches, Grills, Sweets,Chefs,Comment,Contact,Rest_detail
from django.core.exceptions import ValidationError

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


class ChefForm(forms.ModelForm):
    class Meta:
        model = Chefs
        fields = ('__all__')

        # Custom validation for the name field
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3 or len(name) > 250:
            raise forms.ValidationError("Name must be between 3 and 250 characters long.")
        return name

    # Custom validation for the description field
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 100:
            raise forms.ValidationError("Description must between 10 and 99 characters long.")
        return description

    # Custom validation for the image field
    def clean_image(self):
     image = self.cleaned_data.get('image')
     if image:
        # Check if image exists and get its size
        try:
            file_size = image.size
        except AttributeError:
            raise forms.ValidationError("Invalid file uploaded.")
            
        max_size = 5 * 1024 * 1024  # 5 MB
        if file_size > max_size:
            raise forms.ValidationError("Image size must be less than 5MB.")
     return image


    # Custom validation for the social media URLs
    def clean_facebook(self):
        facebook = self.cleaned_data.get('facebook')
        if facebook and len(facebook) > 500:
            raise forms.ValidationError("Facebook URL cannot exceed 500 characters.")
        return facebook

    def clean_instagram(self):
        instagram = self.cleaned_data.get('instagram')
        if instagram and len(instagram) > 500:
            raise forms.ValidationError("Instagram URL cannot exceed 500 characters.")
        return instagram

    def clean_twitter(self):
        twitter = self.cleaned_data.get('twitter')
        if twitter and len(twitter) > 500:
            raise forms.ValidationError("Twitter URL cannot exceed 500 characters.")
        return twitter
    



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Only include the 'text' field since 'user' and 'status' are handled in the view
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['technical_email', 'whatsapp', 'telegram']



class RestDetailForm(forms.ModelForm):
    class Meta:
        model = Rest_detail
        fields = ['name', 'address', 'phone_number', 'email', 'image', 'description1', 'description2']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 255:
            raise ValidationError("Name cannot exceed 255 characters.")
        return name

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) > 255:
            raise ValidationError("Address cannot exceed 255 characters.")
        return address

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) > 20:
            raise ValidationError("Phone number cannot exceed 20 characters.")
        return phone_number

    def clean_description1(self):
        description1 = self.cleaned_data.get('description1')
        if len(description1) > 255:
            raise ValidationError("Description 1 cannot exceed 255 characters.")
        return description1

    def clean_description2(self):
        description2 = self.cleaned_data.get('description2')
        if len(description2) > 1500:
            raise ValidationError("Description 2 cannot exceed 1500 characters.")
        return description2