from django import template
from cart.cart import Cart

register = template.Library()


# декоратор
@register.inclusion_tag('inc/menu_tpl_header.html', takes_context=True)
def header(context, first='first', header__cards='header__cards', container='container'):
    tmp_request = context['request']
    cart = Cart(tmp_request)
    return {"first": first, "header__cards": header__cards, "container": container, "tmp_request": tmp_request, "tmp_cart": cart}
    # return {"first": first, "header__cards": header__cards, "container": container}


@register.inclusion_tag('inc/menu_tpl_footer.html')
def footer(footer='footer'):
    return {"footer": footer}


@register.filter
def to_class_name(value):
    return value.__class__.__name__
