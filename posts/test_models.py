from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(
            username='testuser1', password='12345'
            )
        test_user2 = User.objects.create_user(
            username='testuser2', password='abcdef'
            )
        Post.objects.create(
            owner=test_user1, title='Test Post 1',
            content='This is a test post.'
            )
        Post.objects.create(
            owner=test_user2, title='Test Post 2',
            content='Another test post.', friends_only=True
            )

    def test_post_default_image_filter(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.image_filter, 'normal')

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.id} {post.title} by {post.owner}'
        self.assertEqual(str(post), expected_object_name)
