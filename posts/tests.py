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
        Post.objects.create(owner=test_user, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)


    def test_authenticated_user_can_post(self):
        """
        Test if authenticated users can create posts
        """
        self.client.login(username='test_user', password='qwertyuiopå')
        response = self.client.post('/posts/', {'title': 'test title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_unauthenticated_user_cant_post(self):
        """
        Test if unauthenticated users are unable to post
        """
        response = self.client.post('/posts/', {'title': 'test title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='test_user1', password='pass')
        test_user2 = User.objects.create_user(username='test_user2', password='pass')
        Post.objects.create(
            owner=test_user1, title='test title', content='test_user1s content'
        )
        Post.objects.create(
            owner=test_user2, title='test title2', content='test_user2s content'
        )

    def test_can_retrieve_post_with_valid_id(self):
        """
        Test if posts can be accessed when using a valid post id
        """
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'test title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_with_invalid_id(self):
        """
        Test that posts can NOT be accessed when using an invalid post id
        """
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_owner_can_edit_post(self):
        """
        Test if the owner of a post can update it
        """
        self.client.login(username='test_user1', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_edit_other_users_post(self):
        """
        Test that a user can NOT edit posts by other users
        """
        self.client.login(username='test_user1', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)