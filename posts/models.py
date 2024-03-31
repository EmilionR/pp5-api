from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """
    Model for user posts
    owner refers to the user who posted it
    content is the text content
    friends_only is used for restricting visibility to friends only
    """

    image_filters = [
        ('normal', 'Normal'),
        ('example', 'Example'),
        ('other', 'Other')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    friends_only = models.BooleanField(default=False)
    #  Default image set so that I can always refer to 'image.url'
    image = models.ImageField(
        upload_to='images/', default='../default_post_adbhtw', blank=True
    )
    # Image filter options for when I'll implement them
    image_filter = models.CharField(
        max_length=32, choices=image_filters, default='normal'
    )

    # Order posts by time of posting, starting with the most recent
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title} by {self.owner}'
