from django.db import models
from users.models import Timestamps
from django.conf import settings

# Create your models here.
class Blogs(Timestamps):
    title = models.CharField(max_length=250, null=False)
    content = models.TextField(blank=False, null=False)
    
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')