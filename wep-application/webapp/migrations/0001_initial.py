# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('text2', models.TextField(blank=True, verbose_name='Текст2')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Заголовок2')),
                ('text3', models.TextField(blank=True, verbose_name='Текст3')),
                ('image', models.ImageField(upload_to='images/png', verbose_name='Картинка')),
                ('date', models.DateTimeField(verbose_name='Опубликовано')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Совет дизайнера',
                'verbose_name_plural': 'Советы дизайнера',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('icon', models.ImageField(upload_to='images/png', verbose_name='Икона')),
            ],
            options={
                'verbose_name': 'Звоните на прямую',
                'verbose_name_plural': 'Звоните на прямую',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
                ('icon_for_footer', models.ImageField(upload_to='images/png', verbose_name='Икона для подвала')),
                ('icon_for_page', models.ImageField(upload_to='images/png', verbose_name='Икона для страницы')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/png', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент на странице работы и услуги блок2',
            },
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Координат',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Полное имя')),
                ('position', models.CharField(max_length=150, verbose_name='Должность')),
                ('image', models.ImageField(upload_to='images/jpg', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратные связи',
            },
        ),
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/png', verbose_name='Иконa')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Гарантия',
                'verbose_name_plural': 'Гарантии',
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('icon', models.ImageField(upload_to='images/png', verbose_name='Икона')),
            ],
            options={
                'verbose_name': 'Иконка',
                'verbose_name_plural': 'Иконки',
            },
        ),
        migrations.CreateModel(
            name='LeftBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('icon', models.ImageField(upload_to='images/png', verbose_name='Икона')),
            ],
            options={
                'verbose_name': 'Левая панель',
                'verbose_name_plural': 'Левая панель',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости для рассылок',
            },
        ),
        migrations.CreateModel(
            name='OrderOfMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Заказ мастера',
                'verbose_name_plural': 'Заказ мастера',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
            },
        ),
        migrations.CreateModel(
            name='ProductionFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Особенность',
                'verbose_name_plural': 'Особенности производства',
            },
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=50, verbose_name='Качество')),
            ],
            options={
                'verbose_name': 'Качество',
                'verbose_name_plural': 'Качества',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Полное имя')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Компания')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(null=True, upload_to='images/png', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, upload_to='images/png', verbose_name='Картинка')),
                ('icon', models.ImageField(upload_to='images/png', verbose_name='Икона')),
                ('price', models.CharField(blank=True, max_length=50, verbose_name='Цена')),
                ('term', models.CharField(blank=True, max_length=50, verbose_name='Срок')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('text2', models.TextField(blank=True, verbose_name='Текст2')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/png', verbose_name='Икона')),
                ('link', models.URLField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Ссылка на соц сеть',
                'verbose_name_plural': 'Ссылки на соц сети',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Service', verbose_name='Услуга'),
        ),
    ]
