from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Report(models.Model):
    """
    Report model, for reporting a post
    'owner' is the User who created the report
    'post' is the reported post
    'content' is the reason for the report
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Sort reports by time of creation in descending order
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content