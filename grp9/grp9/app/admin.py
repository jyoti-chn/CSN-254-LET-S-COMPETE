from django.contrib import admin
from .models import(
    Customer,
    Product,
    Carts,
    EventRegistered
)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','brand','category','product_image','eligibility']


@admin.register(Carts)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']


@admin.register(EventRegistered)
class EventRegisteredAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','customer','status']

