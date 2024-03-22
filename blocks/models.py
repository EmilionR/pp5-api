from django.db import models
from django.contrib.auth.models import User


class Block(models.Model):
    """
    Block model, pairing an 'owner' and a 'target', where:
    'owner' is the a User instance, and
    'target' is the User instance to block
    
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order blocks by time of creation
        ordering = ['-created_on']
        # 'unique_together' ensures that users can't block the same user twice
        unique_together = ['owner', 'target']

    def __str__(self):
        return f'{self.owner}, {self.target}'
    