from django.contrib import admin

from .models import Customers, CustomerCustomerDemo, CustomerDemographics


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = (
        'customer_id',
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
    )


@admin.register(CustomerCustomerDemo)
class CustomerCustomerDemoAdmin(admin.ModelAdmin):
    list_display = ('customer', 'customer_type')
    list_filter = ('customer', 'customer_type')


@admin.register(CustomerDemographics)
class CustomerDemographicsAdmin(admin.ModelAdmin):
    list_display = ('customer_type_id', 'customer_desc')
