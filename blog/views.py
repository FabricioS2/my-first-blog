from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect





# Create your views here.

def post_list(request):
    posts = Post.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_criacao') 
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': posts})


def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             Post = form.save(commit=False)
             Post.author = request.user
             Post.published_date = timezone.now()
             Post.save()
             return redirect('post_detail', pk=Post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})




def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})


