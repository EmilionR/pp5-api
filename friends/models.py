from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    """
    Friend model, for befriending other users
    'owner' is a User instance, declaring another User a friend
    'friend' is a User instance chosen as a friend by 'owner'
    """
    owner = models.ForeignKey(
        User, related_name='friender', on_delete=models.CASCADE
    )
    friend = models.ForeignKey(
        User, related_name='friend', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        # prevent duplicate friend instances
        unique_together = ['owner', 'friend']

    def __str__(self):
        return f'{self.owner}, {self.friend}'
