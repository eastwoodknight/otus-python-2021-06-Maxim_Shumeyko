from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, UpdateView, DetailView, TemplateView

from blog_data.models import Post, Author 
from blog_data.forms import PostUpdateForm


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('index')
    form_class = PostUpdateForm


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

    

