from django.contrib import admin

from .models import Categories, Suppliers, Products, OrderDetails, Orders, Shippers


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'description', 'picture')


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = (
        'supplier_id',
        'company_name',
        'contact_name',
        'contact_title',
        'address',
        'city',
        'region',
        'postal_code',
        'country',
        'phone',
        'fax',
        'homepage',
    )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'product_id',
        'product_name',
        'supplier',
        'category',
        'quantity_per_unit',
        'unit_price',
        'units_in_stock',
        'units_on_order',
        'reorder_level',
        'discontinued',
    )


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'unit_price', 'quantity', 'discount')
    raw_id_fields = ('order', 'product')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'customer',
        'employee',
        'order_date',
        'required_date',
        'shipped_date',
        'ship_via',
        'freight',
        'ship_name',
        'ship_address',
        'ship_city',
        'ship_region',
        'ship_postal_code',
        'ship_country',
    )
    list_filter = ('order_date', 'required_date', 'shipped_date')
    raw_id_fields = ('customer', 'employee', 'ship_via')


@admin.register(Shippers)
class ShippersAdmin(admin.ModelAdmin):
    list_display = ('shipper_id', 'company_name', 'phone')
