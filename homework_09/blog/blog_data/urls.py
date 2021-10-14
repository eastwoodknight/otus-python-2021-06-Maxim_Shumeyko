from django.urls import path

from .views import (
    PostList,
    PostDetail,
    PostUpdate,
    TemplateView,
    addpost,
)

urlpatterns = [
    path('', PostList.as_view(), name='index'), 
    path('/post/<int:pk>', PostDetail.as_view(), name='post'),
    path('/post/update/<int:pk>', PostUpdate.as_view(), name='update'),
    path('/about', TemplateView.as_view(template_name='blog_data/about.html'), name='about'),
    path('/add', TemplateView.as_view(template_name='blog_data/add.html'), name='add'),
    path('/addpost', addpost, name='addpost'),
]
