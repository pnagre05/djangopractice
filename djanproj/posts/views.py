from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def posts_lists(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_lists.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})
@login_required(login_url='/users/login/')
def post_new(request):
    if(request.method == "POST"):
        form = forms.CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return posts_lists(request)
    else:
        form = forms.CreatePostForm()
    return render(request, 'posts/post_new.html', {'form': form})