from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)
    cover = models.URLField(max_length=300, default="https://via.placeholder.com/150")

    def __str__(self):
        return self.title