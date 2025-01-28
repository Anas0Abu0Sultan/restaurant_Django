from django.db import models
from PIL import Image
import os

def upload_to_dynamic(instance, filename):
        return f"{instance.__class__.__name__}/{filename}"

class Food(models.Model):
    class Size(models.TextChoices):
        SMALL = 'SM','Small'
        MEDIUM = 'ME','Medium'
        LARG = 'LA','Larg'

    name = models.CharField(max_length=255,blank=False,default='food')
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0.0)
    last_price = models.DecimalField(max_digits=5, decimal_places=2,default=price)
    size = models.CharField(max_length=2,choices=Size.choices,default=Size.SMALL)
    image = models.ImageField(upload_to=upload_to_dynamic,default='media/defa/defa.png')

    class Meta:
        abstract = True 

    def __str__(self):
        return f"{self.name}"


class Drinks(Food):
    class Type_of_drinks(models.TextChoices):
        HOT = 'HO','Hot'
        COLD = 'CO','Cold'
    type_of_drink = models.CharField(max_length=2,choices=Type_of_drinks.choices,default=Type_of_drinks.COLD)

    def __str__(self):
        return f"{self.name} ({self.type_of_drink})"


class Meals(Food):
    def __str__(self):
        return f"{self.name}"

class Sandwiches(Food):
    def __str__(self):
        return f"{self.name}"


class Grills(Food):
        def __str__(self):
         return f"{self.name}"

class Rest_detail(models.Model):
    name = models.CharField(max_length=255,blank=False,default='restaurant')
    address = models.CharField(max_length=255,blank=False,default='address')
    phone_number = models.CharField(max_length=20,blank=False,default='phone_number')
    email = models.EmailField(max_length=255,blank=False,default='email')
    image = models.ImageField(upload_to='restaurant/',default='media/defa/defa.png')

    def __str__(self):
        return f"{self.name}"

class Sweets(Food):
    def __str__(self):
        return f"{self.name}"
    
class Salads(Food):
    def __str__(self):
        return f"{self.name}"

class Clients(models.Model):
    name = models.CharField(max_length=255,blank=False,default='Chef')
    description = models.CharField(max_length=4000,blank=False,default='description Chef')
    image = models.ImageField(upload_to='chef/',default='media/defa/client.png')
    message =models.CharField(max_length=255,blank=False,default='Chef')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
    
class Chefs(models.Model):
    name = models.CharField(max_length=255,blank=False,default='Chef')
    description = models.CharField(max_length=4000,blank=False,default='description Chef')
    image = models.ImageField(upload_to='chef/',default='media/defa/chef.jpg')
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
    

class Services(models.Model):
    name = models.CharField(max_length=50, blank=False, default='Service')
    description = models.CharField(max_length=2500,blank=False,default='description of services')
    icon = models.ImageField(upload_to='icons/')

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


class AboutUs(models.Model):
    paragraph_one = models.CharField(max_length=2500)
    paragraph_two = models.CharField(max_length=2500)
    experience_years = models.PositiveIntegerField(default=15)
    master_chefs = models.PositiveIntegerField(default=50)

class AboutUsImage(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="about_us_images/")