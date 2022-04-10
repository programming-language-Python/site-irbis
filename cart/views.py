from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.apps import apps
from .cart import Cart
from .forms import CartAddProductForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
from . import models


@require_POST
def add_to_cart(request, product_model, product_id):
    # Берём модель в которой находится товар
    Product = apps.get_model('app', product_model)
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['update']:
            cart.update(product, cd['quantity'], product.price)
        else:
            cart.add(Product, product, product.price, cd['quantity'])
    return redirect('cart:cart_detail')


def remove_from_cart(request, product_model, product_id):
    # Берём модель в которой находится товар
    Product = apps.get_model('app', product_model)
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart_detail')


# def clear(request):
#     Cart.clear()
#     return render(request, 'cart/detail.html', {'cart': Cart(request)})


def get_cart(request):
    return render(request, 'cart/detail.html', {'cart': Cart(request)})


def cart_order_number(request):
    if request.method == 'POST':
        cart = Cart(request)
        subject = 'Спасибо за совершение покупки на сайте Pink irbis!'
        html_message = render_to_string(
            'inc/mail_template.html', {'cart': cart})
        plain_message = strip_tags(html_message)
        from_email = 'Pink irbis <{}>'.format(settings.EMAIL_HOST_USER)

        mail = send_mail(subject, plain_message, from_email,
                         [request.user.email], html_message=html_message)
        if True:
            user_is_basket = models.Cart.objects.get(user=request.user)
            data = {}
            for item in cart:
                print(item)
                product = item.product
                title = product.title
                str_model = str(item.content_type)
                model = str(str_model[str_model.rfind('|') + 2:])
                # # формирование JSON
                data[model] = {}
                data[model][title] = cart.cart_serializable()[str(product.id)]
                data[model][title]['unit_price'] = product.price
            json_data = json.dumps(data, ensure_ascii=False, default=str)
            order_number = models.Order_number.objects.create(data=json_data, count=cart.count(), price=cart.summary(),
                                                              cart=user_is_basket)
        # очистка корзины
        cart.clear()
        return render(request, 'cart/detail.html', {'purchase_is_perfect': 'purchase_is_perfect'})
