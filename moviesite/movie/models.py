from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from unicodedata import category
from django import views
from django.db import models
from django.urls import reverse

'''

Category
=========
title, slug

Tag
========
title, slug

Post
=======
Title, logo, slug, content, data_ad, views, category, tags



'''


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


# class Tag(models.Model):
#     title = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['title']


class Quality(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quality', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качество'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    content = models.CharField(max_length=5000, verbose_name='Описание')
    urlmov = models.CharField(max_length=500, verbose_name='Ссылка на видео')
    data_ad = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='movies', verbose_name='Категория')
    # tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    released = models.CharField(default='None', max_length=15, verbose_name='Год выхода')
    director = models.CharField(default='None', max_length=50, verbose_name='Режиссер')
    side = models.CharField(default='None', max_length=50, verbose_name='Страна', blank=True, null=True)
    actors = models.CharField(default='None', max_length=5000, verbose_name='Актеры', blank=True, null=True)
    genre = models.CharField(default='None', max_length=3000, verbose_name='Жанр', blank=True, null=True)
    translation = models.CharField(default='None', max_length=3000, verbose_name='Перевод')
    quality = models.ForeignKey(Quality, default='None', on_delete=models.PROTECT, related_name='movies',
                                verbose_name='Качество')
    rateKP = models.CharField(default='None', max_length=3000, verbose_name='Рейтинг КП')
    rateIMDB = models.CharField(default='None', max_length=3000, verbose_name='Рейтинг IMDB')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-data_ad']
