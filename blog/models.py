# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal
from django.db import models
from django.utils import timezone
from PIL import Image  

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to='images', blank=True, verbose_name='Загрузить изображение поста')
    title = models.CharField(max_length=400)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
