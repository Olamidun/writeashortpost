from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    """def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 3264 or img.width > 2448:
            output_size = (3264, 2448)
            img.thumbnail(output_size)
            img.save(self.image.path)
    """