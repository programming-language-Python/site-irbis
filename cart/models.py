from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

# Create your models here.
from app.models import Menu


class Order_number(models.Model):
    data = models.JSONField(verbose_name='Заказано')
    count = models.IntegerField(default=0, verbose_name='Количество товаров')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата заказа')
    cart = models.ForeignKey(
        'Cart', on_delete=models.PROTECT, verbose_name='Заказчик')
    checked_out = models.BooleanField(
        default=False, verbose_name=_('checked out'))

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Номер заказа'
        verbose_name_plural = 'Номера заказов'
        ordering = ['id']


class Cart(models.Model):
    # creation_date = models.DateTimeField(verbose_name=_('creation date'))
    # checked_out = models.BooleanField(
    #     default=False, verbose_name=_('checked out'))

    # class Meta:
    #     verbose_name = _('cart')
    #     verbose_name_plural = _('carts')
    #     ordering = ('-creation_date',)

    # def __unicode__(self):
    #     return unicode(self.creation_date)
    # key = models.TextField(verbose_name='Ключ')
    # data = models.JSONField(null=True, blank=True, verbose_name='Данные')
    # count = models.IntegerField(default=0, verbose_name='Покупки')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    total_count = models.IntegerField(
        default=0, verbose_name='Общее количество')
    total_price = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, verbose_name='Общая сумма')

    # checked_out = models.BooleanField(
    #     default=False, verbose_name=_('checked out'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('id',)

    def __str__(self):
        return str(self.id)


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(
                type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del (kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(
                type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del (kwargs['product'])
        return super(ItemManager, self).filter(*args, **kwargs)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_(
        'cart'), on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Наименование')
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(
        max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price

    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)
