from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from blog_data.models import Post, Author 

def index(request):
#    return HttpResponse("Empty for now. Work in progress...")
    posts = Post.objects.all()
    return render(request, 'blog_data/index.html', {'posts': posts,})


def about(request):
    return render(request, 'blog_data/about.html')


def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog_data/post.html', {'post': post})


def add(request):
    return render(request, 'blog_data/add.html',)
                  

def addpost(request):
    title = request.POST.get('title')
    subtitle = request.POST.get('subtitle')
    author_name = request.POST.get('author')
    content = request.POST.get('content')

    try:
        author = Author.objects.get(name=author_name)
    except ObjectDoesNotExist: 
        author = Author(name=author_name)
        author.save()

    post = Post(
        title=title,
        subtitle=subtitle,
        author=author,
        content=content,
    )
    post.save()

    return index(request)

    

