from django.db import models

from django.db import models

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
