from django.urls import path

from .views import (
    index, 
    about,
    post,
    add,
    addpost,
)

urlpatterns = [
    path('', index, name='index'), 
    path('/about', about, name='about'),
    path('/post/<int:post_id>', post, name='post'),
    path('/add', add, name='add'),
    path('/addpost', addpost, name='addpost'),
]
