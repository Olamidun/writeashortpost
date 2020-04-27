from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'post_image')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
# admin.site.register(PostPicture)
