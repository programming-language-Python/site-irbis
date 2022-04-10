from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from irbis.settings import MEDIA_URL


# from django.contrib.contenttypes.models import ContentType

# Create your models here.


class Numbers(models.Model):
    class Enum(models.TextChoices):
        one = '1', _('1-но комнатный')
        two = '2', _('2-х комнатный')
        three = '3', _('3-х комнатный')
        four = '4', _('4-х комнатный')

    enum = models.CharField(
        max_length=1, choices=Enum.choices, default=Enum.one, )
    title = models.CharField(max_length=150, verbose_name='Наименование')
    subscrible = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    img = models.ImageField(upload_to='photos/Номера/',
                            verbose_name='Фото')

    def del_html_tag_in_subscrible(self):
        return mark_safe(self.subscrible)

    def get_absolute_url(self):
        return reverse('app:card_numbers', kwargs={"number_id": self.pk})

    def __str__(self):
        return str(self.id)

    def get_img(self):
        return MEDIA_URL + str(self.img)

    # для админки
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
        ordering = ['id']


class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id']


class Excursion(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    subscrible = models.TextField(verbose_name='Описание')
    program = models.TextField(verbose_name='Программа')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    img = models.ImageField(upload_to='photos/Экскурсии/',
                            verbose_name='Фото')

    def del_html_tag_in_subscrible(self):
        return mark_safe(self.subscrible)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('app:card_excursion', kwargs={"excursion_id": self.pk})

    def get_img(self):
        return MEDIA_URL + str(self.img)

    class Meta:
        verbose_name = 'Экскурссия'
        verbose_name_plural = 'Экскурссии'
        ordering = ['id']


class Menu(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    subscrible = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    img = models.ImageField(upload_to='photos/Меню/',
                            verbose_name='Фото')

    def del_html_tag_in_subscrible(self):
        return mark_safe(self.subscrible)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('app:card_menu', kwargs={"menu_id": self.pk})

    def get_img(self):
        return MEDIA_URL + str(self.img)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['id']
