# from decimal import Decimal
# from django.conf import settings
# from django.apps import apps
# from app.models import Numbers, Service, Excursion, Menu, Cart
# from django.contrib.sessions.models import Session

import datetime
from django.db.models import Sum
from django.db.models import F, FloatField
from . import models

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        # * Проверяем была ли у пользователя сессия
        if request.user.is_authenticated:
            cart = models.Cart.objects.filter(user=request.user).first()
            if cart is None:
                # * создаём данные корзины
                cart = self.new(request)
        elif cart_id:
            cart = models.Cart.objects.filter(
                id=cart_id).first()
            if cart is None:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        if str(request.user) == 'AnonymousUser':
            cart = models.Cart.objects.create()
        else:
            cart = models.Cart.objects.create(user=request.user)
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product_model, product, unit_price, quantity=1):
        item = models.Item.objects.filter(
            cart=self.cart, product=product).first()
        if item:
            item.unit_price = unit_price
            item.quantity += int(quantity)
            item.save()
        else:
            models.Item.objects.create(
                cart=self.cart, product=product, title=product.title, unit_price=unit_price, quantity=quantity)

    def remove(self, product):
        item = models.Item.objects.filter(
            cart=self.cart, product=product).first()
        if item:
            item.delete()
        else:
            raise ItemDoesNotExist

    def update(self, product, quantity, unit_price=None):
        item = models.Item.objects.filter(
            cart=self.cart, product=product).first()
        if item:
            if quantity == 0:
                item.delete()
            else:
                item.unit_price = unit_price
                item.quantity = int(quantity)
                item.save()
        else:
            raise ItemDoesNotExist

    def count(self):
        return self.cart.item_set.all().aggregate(Sum('quantity')).get('quantity__sum', 0)

    def summary(self):
        return self.cart.item_set.all().aggregate(
            total=Sum(F('quantity') * F('unit_price'), output_field=FloatField())).get('total', 0)

    def clear(self):
        self.cart.item_set.all().delete()
        # * очищаем корзину в сессии
        # del self.session[CART_ID]
        # self.save()

    def is_empty(self):
        return self.count() == 0

    def cart_serializable(self):
        representation = {}
        for item in self.cart.item_set.all():
            item_id = str(item.object_id)
            item_dict = {
                'total_price': item.total_price,
                'quantity': item.quantity
            }
            representation[item_id] = item_dict
        return representation
