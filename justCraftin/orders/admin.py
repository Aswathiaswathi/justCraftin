from django.contrib import admin
from . models import CartOrder,OrderedItem

# Register your models here.

admin.site.register(OrderedItem)
class OrderAdmin(admin.ModelAdmin):
    list_filter=['owner','order_status']
    search_fields=["owner","id",]
admin.site.register(CartOrder,OrderAdmin)
