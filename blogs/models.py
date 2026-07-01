from django.db import models
from users.models import Timestamps, Users

# Create your models here.
class Blogs(Timestamps):
    title = models.CharField(max_length=250, null=False)
    content = models.TextField(blank=False, null=False)
    
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='blogs')