from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('article title', max_length=200)
    article_text = models.TextField('article text')
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Block of articles'
        verbose_name_plural = 'Blocks of articles'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('author name', max_length=100)
    comment_text = models.CharField('comment text', max_length=400)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
