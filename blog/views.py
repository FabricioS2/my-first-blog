from django.shortcuts import render
from .models import post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = post.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_criacao') 
    return render(request, 'blog/post_list.html', {'posts':posts})
