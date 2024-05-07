from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import CustomUser


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class News(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(CustomUser, default=None, blank=True,related_name='liked_news')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    news_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)



class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    value = models.CharField(default="Like",choices=LIKE_CHOICES, max_length=10)

    def __str__(self):
        return self.news.title

