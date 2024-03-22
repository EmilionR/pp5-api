from django.db import models
from posts.models import Post
from django.contrib.auth.models import User


class Like(models.Model):
    """
    Like model, pairing an 'owner' and a 'post', where:
    'owner' is a User instance
    'post' is a Post instance.
    'unique_together' ensures that users can't like the same post twice
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'