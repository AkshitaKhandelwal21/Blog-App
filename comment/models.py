from django.db import models
from blogs.models import Blogs
from users.models import Users

# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name="comments")
    