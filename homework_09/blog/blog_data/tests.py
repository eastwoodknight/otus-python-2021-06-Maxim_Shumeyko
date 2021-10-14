from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from .models import Post, Author

class SimpleViewTest(SimpleTestCase):
    
    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)



class ViewTest(TestCase):

    author_data = {'name': "Guido",}
    post_data = {
        'title': "Title",
        'subtitle': "subtitle",
        'content': "content",
    }

    def setUp(self):
        author_data = self.author_data
        post_data = self.post_data

        author = Author.objects.create(name=author_data['name'])
        post = Post.objects.create(
            title=post_data['title'],
            subtitle=post_data['subtitle'], 
            content=post_data['content'],
            author=author,
        )

    def tearDown(self):
        Post.objects.all().delete()
        Author.objects.all().delete()

    def test_index(self):
        author_data = self.author_data
        post_data = self.post_data

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        self.assertIn(author_data['name'].encode(), response.content)
        self.assertIn(post_data['title'].encode(), response.content)
        self.assertIn(post_data['subtitle'].encode(), response.content)
        self.assertIn(post_data['content'].encode(), response.content)

    def test_addpost(self):
        Post.objects.all().delete()
        Author.objects.all().delete()

        author_data = self.author_data
        post_data = self.post_data

        response = self.client.post(
            reverse('addpost'),
            data = {
                'title': post_data['title'],
                'subtitle': post_data['subtitle'],
                'content': post_data['content'],
                'author': author_data['name'],
            },
        )

        self.assertRedirects(response, reverse('index'))
        self.assertTrue(Post.objects.count() == 1)
                
                

        

        
