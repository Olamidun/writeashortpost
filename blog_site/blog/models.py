from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # post_image = CloudinaryField('post_pics', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_thumbs_up = models.IntegerField(default=0)
    user_thumbs_up = models.ManyToManyField(User, related_name='thumbs_up')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    owner = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text






