from django.db import models
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField


class Call(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Заголовок'))
    phone = models.CharField(max_length=50, verbose_name=_('Телефон'))
    icon = models.ImageField(upload_to='images/png', verbose_name=_('Икона'))

    class Meta:
        verbose_name = _('Звоните на прямую')
        verbose_name_plural = _('Звоните на прямую')


class Quality(models.Model):
    quality = models.CharField(max_length=50, verbose_name=_('Качество'))

    class Meta:
        verbose_name = _('Качество')
        verbose_name_plural = _('Качества')


class Icon(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Заголовок'))
    description = models.CharField(max_length=200, verbose_name=_('Описание'))
    icon = models.ImageField(upload_to='images/png', verbose_name=_('Икона'))

    class Meta:
        verbose_name = _('Иконка')
        verbose_name_plural = _('Иконки')


class LeftBar(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Заголовок'))
    description = models.CharField(max_length=200, verbose_name=_('Описание'))
    icon = models.ImageField(upload_to='images/png', verbose_name=_('Икона'))

    class Meta:
        verbose_name = _('Левая панель')
        verbose_name_plural = _('Левая панель')


class Review(models.Model):
    full_name = models.CharField(max_length=50, verbose_name=_('Полное имя'))
    company = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Компания'))
    text = models.TextField(verbose_name=_('Текст'))
    image = models.ImageField(upload_to='images/png', null=True, verbose_name=_('Фото'))

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')


class Contact(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    description = models.CharField(max_length=150, verbose_name=_('Описание'))
    icon_for_footer = models.ImageField(upload_to='images/png', verbose_name=_('Икона для подвала'))
    icon_for_page = models.ImageField(upload_to='images/png', verbose_name=_('Икона для страницы'))

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')


class Advice(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Заголовок'))
    text = models.TextField(verbose_name=_('Текст'))
    text2 = models.TextField(blank=True, verbose_name=_('Текст2'))
    title2 = models.CharField(max_length=50, blank=True, verbose_name=_('Заголовок2'))
    text3 = models.TextField(blank=True, verbose_name=_('Текст3'))
    image = models.ImageField(upload_to='images/png', verbose_name=_('Картинка'))
    date = models.DateTimeField(verbose_name=_('Опубликовано'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('Слаг'))

    class Meta:
        verbose_name = _('Совет дизайнера')
        verbose_name_plural = _('Советы дизайнера')


class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Заголовок'))
    image = models.ImageField(upload_to='images/png', blank=True, verbose_name=_('Картинка'))
    icon = models.ImageField(upload_to='images/png', verbose_name=_('Икона'))
    price = models.CharField(max_length=50, blank=True, verbose_name=_('Цена'))
    term = models.CharField(max_length=50, blank=True, verbose_name=_('Срок'))
    text = models.TextField(blank=True, verbose_name=_('Текст'))
    text2 = models.TextField(blank=True, verbose_name=_('Текст2'))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_('Слаг'))

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Имя'))
    phone = models.CharField(max_length=50, verbose_name=_('Телефон'))
    message = models.TextField(verbose_name=_('Сообщение'))
    service = models.ForeignKey(Service, null=True, blank=True, verbose_name=_('Услуга'))

    class Meta:
        verbose_name = _('Обратная связь')
        verbose_name_plural = _('Обратные связи')


class OrderOfMaster(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Имя'))
    phone = models.CharField(max_length=50, verbose_name=_('Телефон'))

    class Meta:
        verbose_name = _('Заказ мастера')
        verbose_name_plural = _('Заказ мастера')


class Content(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'))
    image = models.ImageField(upload_to="images/png", verbose_name=_('Картинка'))

    class Meta:
        verbose_name = _('Контент')
        verbose_name_plural = _('Контент на странице работы и услуги блок2')


class ProductionFeature(models.Model):
    description = models.TextField(verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Особенность')
        verbose_name_plural = _('Особенности производства')

    def __str__(self):
        return self.description


class Employee(models.Model):
    full_name = models.CharField(max_length=150, verbose_name=_('Полное имя'))
    position = models.CharField(max_length=150, verbose_name=_('Должность'))
    image = models.ImageField(upload_to='images/jpg', verbose_name=_('Фото'))

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'))
    date = models.DateTimeField(verbose_name=_('Опубликовано'))

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости для рассылок')


class Subscriber(models.Model):
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = _('Подписчик')
        verbose_name_plural = _('Подписчики')

    def __str__(self):
        return self.email


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')


class Guarantee(models.Model):
    image = models.ImageField(upload_to='images/png', verbose_name=_('Иконa'))
    description = models.TextField(verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Гарантия')
        verbose_name_plural = _('Гарантии')


class OurTeam(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Наша команда')
        verbose_name_plural = _('Наша команда')


class SocialLink(models.Model):
    icon = models.ImageField(upload_to='images/png', verbose_name=_('Икона'))
    link = models.URLField(verbose_name=_('Ссылка'))

    class Meta:
        verbose_name = _('Ссылка на соц сеть')
        verbose_name_plural = _('Ссылки на соц сети')


class Coordinate(models.Model):
    address = models.CharField(max_length=100, verbose_name=_('адрес'))
    position = GeopositionField(verbose_name=_('Координаты'))

    class Meta:
        verbose_name = _("Координат")
        verbose_name_plural = _("Координаты")
