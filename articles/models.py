from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class News(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='news_photos/')
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class VideoPost(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.utils import timezone

uploaded_at = models.DateTimeField(auto_now_add=True, default=timezone.now)









