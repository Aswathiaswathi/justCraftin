from django import template

register=template.Library()
@register.simple_tag(name='get_total')
def get_total(cart):
    total=0
    for item in cart.added_items.all():
        total=total+item.quantity*item.product.price
    return total