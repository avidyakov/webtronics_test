from django.conf import settings
from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel


class Post(TitleSlugDescriptionModel, TimeStampedModel, models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
