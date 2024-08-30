from django.db import models
from customers.models import Customer
from products.models import Product

# model for cartOrder

class CartOrder(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECED=4
    STATUS_CHOICE=((ORDER_CONFIRMED,'ORDER_CONFIRMED'),(ORDER_PROCESSED,'ORDER_PROCESSED'),(ORDER_DELIVERED,'ORDER_DELIVERED'),(ORDER_REJECED,'ORDER_REJECED'))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self)-> str:
        return "order-{}-{}".format(self.id,self.owner.user.username)

#model for Ordereditem

class OrderedItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='added_carts')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(CartOrder,on_delete=models.CASCADE,related_name='added_items')


