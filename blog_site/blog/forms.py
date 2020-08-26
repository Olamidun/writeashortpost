from django import forms
from .models import Post, Comment
from cloudinary.forms import CloudinaryFileField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    # post_image = CloudinaryFileField(
    #     options={
    #         'folder': 'post_pics'
    #     }, required=False
    # )
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2 mr-1',
            'placeholder': 'Title'

        }
    ))
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ('title', 'content')


"""
class PostPictureForm(forms.ModelForm):
    post_image = CloudinaryFileField(
        options={
            'folder': 'post_pics'
        }
    )
    


    class Meta:
        model = PostPicture
        fields = ('post_image',)
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('owner', 'text')
