from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse

class CustomUser(AbstractUser):
    def get_absolute_url(self):
        return reverse('profile_detail', args=[self.username])

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='D:\Django\poem_platform\accounts\static\avatar.png') 

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Poem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='poems')
    tags = models.ManyToManyField('Tag', related_name='poems')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_poems', blank=True)
    comments = models.ManyToManyField('Comment', related_name='poems', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} on {self.poem.title}"
    
class Like(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, related_name='liked_by')
    # Rename related_name from 'likes' to 'liked_by'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user} on {self.poem.title}"
