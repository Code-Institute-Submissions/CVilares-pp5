from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateField(auto_now_add=True)
    update_on = models.DateField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
   
