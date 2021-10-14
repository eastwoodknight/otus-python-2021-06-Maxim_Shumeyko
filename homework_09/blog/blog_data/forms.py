from django.forms import ModelForm

from blog_data.models import Post

class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

