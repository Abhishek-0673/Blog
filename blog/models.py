from django.db import models
from datetime import datetime

from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255,unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now())
    def __str__(self):
       return self.title

    class Meta:
        verbose_name_plural = 'Post'
        ordering= ['-created']
        def __unicode__(self):
            return u'%s'% self.title
    def get_absolute_url(self):
        return reverse('blog.views.post',args=[self.slug])



