from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title