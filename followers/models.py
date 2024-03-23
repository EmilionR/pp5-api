from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, for following other users
    'follower' is a User instance, which is following another User instance.
    'followed' is a User instance being followed by 'follower'.
    """
    follower = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        # prevent duplicate follower instances
        unique_together = ['follower', 'followed']

    def __str__(self):
        return f'{self.follower} follows {self.followed}'