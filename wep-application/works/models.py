from django.db import models
from django.utils.translation import ugettext_lazy as _


class Filter(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Заголовок'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('Слаг'))

    class Meta:
        verbose_name = _('Фильтр')
        verbose_name_plural = _('Фильтры')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    icon = models.ImageField(upload_to='images/png', verbose_name=_('Картинка'))
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title


class Catalog(models.Model):
    image = models.ImageField(upload_to='images/jpg', verbose_name=_('Картинка'))
    filter = models.ForeignKey(Filter, verbose_name=_('Фильтр'))
    text = models.TextField(blank=True, verbose_name=_('Текст'))

    class Meta:
        verbose_name = _('Каталог')
        verbose_name_plural = _('Каталог')


class Style(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))

    class Meta:
        verbose_name = _('Стиль')
        verbose_name_plural = _('Стили')

    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'))
    image = models.ImageField(upload_to='images/jpg', verbose_name=_('Картинка'))
    filter = models.ForeignKey(Filter, verbose_name=_('Фильтр'))
    category = models.ForeignKey(Category, verbose_name=_('Категория'))
    style = models.ForeignKey(Style, verbose_name=_('Стиль'))
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = _('Робота')
        verbose_name_plural = _('Работы')

    def __str__(self):
        return str(self.title)
