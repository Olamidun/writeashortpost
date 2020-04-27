from django import forms
from blog.models import Post, Comment
from cloudinary.forms import CloudinaryFileField


class PostForm(forms.ModelForm):
    post_image = CloudinaryFileField(
        options={
            'folder': 'post_pics'
        }, required=False
    )
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2 mr-1',
            'placeholder': 'Title'

        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control mb-2 mr-1',
            'placeholder': 'Write an article...'
        }
    ))

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_image')


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
