from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-date',]