from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test_user', password='qwertyuiopå')

    def test_post_list(self):
        """
        Test if the post list works
        """
        test_user = User.objects.get(username='test_user')
        Post.objects.create(owner=test_user, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

