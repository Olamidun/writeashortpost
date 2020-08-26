from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.


def home(request):
    post = Post.objects.all().order_by('-date_posted')
    query = request.GET.get('q')
    if query:
        post = post.filter(
            Q(title__icontains=query) | Q(content__icontains=query) |
            Q(author__username__icontains=query)

        ).distinct()
        if not post.exists():
            return render(request, 'blog/no_result.html', {})
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/home.html', {'posts': posts})


def user_list(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})


def user_post_list(request, username):
    user = get_object_or_404(User, username=username)
    post = Post.objects.filter(author=user).order_by('-date_posted')
    query = request.GET.get('q')
    if query:
        post = post.filter(Q(title__icontains=query)).distinct()
    page = request.GET.get('page')
    paginator = Paginator(post, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/user_post.html', {'posts': posts})


@login_required
def post_details(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    # post_pictures = PostPicture.objects.filter(post_image='D0buc_5WsAAPMUE.jpeg')
    all_comments = Comment.objects.filter(post=posts)
    form = CommentForm()
    if request.method == 'POST':
        new_owner = request.POST['owner']
        new_text = request.POST['text']
        new_comment = Comment.objects.create(owner=new_owner, text=new_text, post=posts)
        return redirect('post-detail', pk=posts.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'posts': posts, 'all_comments': all_comments})
                                                     # 'post_pictures': post_pictures}


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.author = request.user
            temp.save()
        return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/blog_form.html', {'form': form})


@login_required
def update_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.user == posts.author or request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=posts)
            if form.is_valid():
                form.save()
                return redirect('blog-home')
        else:
            form = PostForm(instance=posts)
    else:
        return HttpResponse('Permission denied')
    return render(request, 'blog/post_update.html', {'form': form, })


@login_required
def delete_post(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.user == posts.author or request.user.is_superuser:
        if request.method == 'POST':
            posts.delete()
            return redirect('blog-home')
        else:
            return render(request, 'blog/post_delete.html', {})
    else:
        return HttpResponse('Permission Denied!')


@login_required
def post_thumbs_up(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    post.number_of_thumbs_up += 1
    post.user_thumbs_up.add(user)
    post.save()
    return redirect('blog-home')


@login_required
def remove_post_thumbs_up(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    post.user_thumbs_up.remove(user)
    post.number_of_thumbs_up -= 1
    post.save()
    return redirect('blog-home')


@login_required
def recent_post(request):
    posts = Post.objects.filter(date_posted__lte=timezone.now()).order_by('-date_posted')[:8]
    return render(request, 'blog/recent_post.html', {'posts': posts})


def privacy_policy(request):
    return render(request, 'blog/privacy_policy.html', {})

