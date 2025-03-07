from django.db import models
from PIL import Image
import os
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import random

#                             <<<<<     FOOD    >>>>>

def upload_to_dynamic(instance, filename):
        return f"{instance.__class__.__name__}/{filename}"

class Food(models.Model):
    name = models.CharField(max_length=255,blank=False,default='food')
    price = models.DecimalField(max_digits=6, decimal_places=2,default=0.0)
    image = models.ImageField(upload_to=upload_to_dynamic,default='defa/defa.png')
    description = models.CharField(max_length=255,blank=False,default='description')
    # category = models.CharField(max_length=250,blank=False,default='food_menu')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize the image
        if self.image:
            img_path = self.image.path
            with Image.open(img_path) as img:
                    output_size = (90, 90)
                    img = img.resize(output_size, Image.Resampling.LANCZOS)
                    img.save(img_path)

    class Meta:
        abstract = True 

    def __str__(self):
        return f"{self.name}"
    def get_class_name(self):
        return self.__class__.__name__  # Returns the model name as a string
    
class SizePriceMixin(models.Model):
    class Size(models.TextChoices):
        SMALL = 'SM', 'Small'
        MEDIUM = 'ME', 'Medium'
        LARGE = 'LA', 'Large'

    size = models.CharField(max_length=2, choices=Size.choices, default=Size.SMALL)
    small_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    medium_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    large_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    class Meta:
        abstract = True

    def get_price_by_size(self, size):
        """Return the correct price based on the selected size."""
        if size == self.Size.SMALL:
            return self.small_price
        elif size == self.Size.MEDIUM:
            return self.medium_price
        elif size == self.Size.LARGE:
            return self.large_price
        return self.small_price



class Drinks(Food, SizePriceMixin):
    class TypeOfDrinks(models.TextChoices):
        HOT = 'HO', 'Hot'
        COLD = 'CO', 'Cold'

    type_of_drink = models.CharField(max_length=2, choices=TypeOfDrinks.choices, default=TypeOfDrinks.COLD)

    def __str__(self):
        return f"{self.name} - {self.get_price_by_size(self.size)}"

class Salads(Food, SizePriceMixin):
    def __str__(self):
        return f"{self.name} - {self.get_price_by_size(self.size)}"


class Meals(Food):
    def __str__(self):
        return f"{self.name}"

class Sandwiches(Food):
    def __str__(self):
        return f"{self.name}"


class Grills(Food):
        def __str__(self):
         return f"{self.name}"
        
class Sweets(Food):
    def __str__(self):
        return f"{self.name}"
    

#                             <<<<<     Clients    >>>>>


# class Clients(models.Model):
#     name = models.CharField(max_length=255,blank=False,default='Chef')
#     description = models.CharField(max_length=4000,blank=False,default='description Chef')
#     image = models.ImageField(upload_to='chef/',default='defa/client.png')
#     message =models.CharField(max_length=255,blank=False,default='Chef')
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-date']

#     def __str__(self):
#         return self.name


class Comment(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=4000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at}'


#                             <<<<<     Chefs    >>>>>

class Chefs(models.Model):
    name = models.CharField(max_length=255,blank=False,default='Chef')
    description = models.CharField(max_length=4000,blank=False,default='description Chef')
    image = models.ImageField(upload_to='chef/',default='defa/chef.jpg')
    facebook = models.URLField(max_length=500, blank=True, default='', help_text="URL to the chef's Facebook profile")
    instagram = models.URLField(max_length=500, blank=True, default='', help_text="URL to the chef's Instagram profile")
    twitter = models.URLField(max_length=500, blank=True, default='', help_text="URL to the chef's Twitter profile")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize the image
        if self.image:
            img_path = self.image.path
            with Image.open(img_path) as img:
                if img.height > 400 or img.width > 400:  # Adjust dimensions as needed
                    output_size = (400, 400)
                    img = img.resize(output_size, Image.Resampling.LANCZOS)
                    img.save(img_path)


    def __str__(self):
        return self.name
    

#                             <<<<<     Services    >>>>>

class Services(models.Model):
    name = models.CharField(max_length=50, blank=False, default='Service')
    description = models.CharField(max_length=2500,blank=False,default='description of services')
    icon = models.ImageField(upload_to='icons/',default='defa/client.png')
    text_icon = models.CharField(max_length=2500,default='fa fa-3x fa-cart-plus text-primary mb-4')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize the image
        if self.icon:
            img_path = self.icon.path
            with Image.open(img_path) as img:
                if img.height > 300 or img.width > 300:  # Adjust dimensions as needed
                    output_size = (300, 300)
                    img = img.resize(output_size, Image.Resampling.LANCZOS)
                    img.save(img_path)


#                             <<<<<     AboutUs    >>>>>

class AboutUs(models.Model):
    paragraph_one = models.CharField(max_length=2500)
    paragraph_two = models.CharField(max_length=2500)
    experience_years = models.PositiveIntegerField(default=15)
    master_chefs = models.PositiveIntegerField(default=50)

class AboutUsImage(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="about_us_images/")

#                             <<<<<     Contact    >>>>>

class Contact(models.Model):
    booking_email = models.EmailField(default='anas227sultan@gmail.com')
    general_email = models.EmailField(default='anas227sultan@gmail.com')
    technical_email = models.EmailField(default='anas227sultan@gmail.com')
    whatsapp = models.CharField(max_length=15, default='+972594073606')
    telegram = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Contact - Booking: {self.booking_email}, WhatsApp: {self.whatsapp}"

#                             <<<<<     rest_deta    >>>>>

class Rest_detail(models.Model):
    name = models.CharField(max_length=255,blank=False,default='restaurant')
    address = models.CharField(max_length=255,blank=False,default='address')
    phone_number = models.CharField(max_length=20,blank=False,default='phone_number')
    email = models.EmailField(max_length=255,blank=False,default='email')
    image = models.ImageField(upload_to='restaurant/',default='defa/defa.png')
    description1 = models.CharField(max_length=255,default='Enjoy OurDelicious Meal')
    description2 = models.CharField(max_length=1500,default='Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit. Aliqu diam amet diam et eos. Clita erat ipsum et lorem et sit, sed stet lorem sit clita duo justo magna dolore erat amet')
    video_url = models.URLField(default='https://www.youtube.com/watch?v=LXNdRCjZt00&t=19s')
    background_image_url = models.ImageField(upload_to='restaurant/backgrounds/', default='defa/background.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize the image
        if self.image:
            img_path = self.image.path
            with Image.open(img_path) as img:
                # if img.height > 400 or img.width > 400:  # Adjust dimensions as needed
                    output_size = (500, 500)
                    img = img.resize(output_size, Image.Resampling.LANCZOS)
                    img.save(img_path)

    def __str__(self):
        return f"{self.name}"



#                             <<<<<     Cart    >>>>>
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    state = models.CharField(max_length=100, blank=True,null=True)
    street = models.CharField(max_length=255, blank=True,null=True)
    phone = models.CharField(max_length=15, blank=True,null=True)
    secret_number = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('completed', 'Completed')],
        default='active',
    )
    def save(self, *args, **kwargs):
        if not self.secret_number:  # Generate only if not set
            self.secret_number = random.randint(1000, 9999)  # 4-digit number
        super().save(*args, **kwargs)


    def total_items(self):
        return self.cart_items.count()

    def __str__(self):
        return f"Cart {self.id} - {self.user if self.user else 'Guest'}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #This stores the type of model (e.g., Drinks, Meals, etc.).
    object_id = models.PositiveIntegerField()
    food_item = GenericForeignKey("content_type", "object_id") # This creates a dynamic reference to any food model using content_type and object_id.
    size = models.CharField(max_length=2, choices=SizePriceMixin.Size.choices, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    
    def clean(self):
        # Ensure food_item exists
        if self.food_item is None:
            raise ValidationError("The referenced food item does not exist.")

    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity}x {self.food_item.name} ({self.size if self.size else 'No Size'})"

#                             <<<<<     CartItem    >>>>>


