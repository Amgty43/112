from django.db import models
from django.urls import reverse


class Post(models.Model):       #Inheritance/post extend models
    title = models.CharField(max_length=128) #compsition: post is composed of other classes
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("details", args=[self.id])

