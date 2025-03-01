from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='account')
    job_title = models.CharField(max_length=255, blank=True, default='Client')
    image = models.ImageField(upload_to='clients/', default='defa/client.png')  # Add profile image
    credits = models.SmallIntegerField(default=0)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Resize the image
        if self.image:
            img_path = self.image.path
            with Image.open(img_path) as img:
                    output_size = (50, 50)
                    img = img.resize(output_size, Image.Resampling.LANCZOS)
                    img.save(img_path)

    def __str__(self):
        return f'{self.user.username} account'
    
    