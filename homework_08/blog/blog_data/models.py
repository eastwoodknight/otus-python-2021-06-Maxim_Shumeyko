from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True, db_index=True)
    content = models.TextField()
    
    author = models.ForeignKey(
        Author, 
        on_delete=models.PROTECT,
        related_name='posts',
    )

    class Meta:
        ordering = ['date_posted']

