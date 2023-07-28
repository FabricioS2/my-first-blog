from django.shortcuts import render
from .models import post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.

def post_list(request):
    posts = post.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_criacao') 
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    posts = get_object_or_404(post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': posts})
