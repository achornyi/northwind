from django.db import models

from customers.models import Customers
from employee.models import Employees


# Create your models here.
class Categories(models.Model):
    category_id = models.SmallIntegerField(primary_key=True)
    category_name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Suppliers(models.Model):
    supplier_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'suppliers'
        verbose_name = 'suppliers'
        verbose_name_plural = 'suppliers'

    def __str__(self):
        return self.company_name


class Products(models.Model):
    product_id = models.SmallIntegerField(primary_key=True)
    product_name = models.CharField(max_length=40)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    quantity_per_unit = models.CharField(max_length=20, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    units_in_stock = models.SmallIntegerField(blank=True, null=True)
    units_on_order = models.SmallIntegerField(blank=True, null=True)
    reorder_level = models.SmallIntegerField(blank=True, null=True)
    discontinued = models.IntegerField()

    class Meta:
        db_table = 'products'
        verbose_name = 'products'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.product_name


class OrderDetails(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    unit_price = models.FloatField()
    quantity = models.SmallIntegerField()
    discount = models.FloatField()

    class Meta:
        db_table = 'order_details'
        unique_together = (('order', 'product'),)
        verbose_name = 'order details'
        verbose_name_plural = 'order details'

    def __str__(self):
        return self.order


class Orders(models.Model):
    order_id = models.SmallIntegerField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    required_date = models.DateField(blank=True, null=True)
    shipped_date = models.DateField(blank=True, null=True)
    ship_via = models.ForeignKey('Shippers', models.DO_NOTHING, db_column='ship_via', blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)
    ship_name = models.CharField(max_length=40, blank=True, null=True)
    ship_address = models.CharField(max_length=60, blank=True, null=True)
    ship_city = models.CharField(max_length=15, blank=True, null=True)
    ship_region = models.CharField(max_length=15, blank=True, null=True)
    ship_postal_code = models.CharField(max_length=10, blank=True, null=True)
    ship_country = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'orders'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.order_id


class Shippers(models.Model):
    shipper_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        db_table = 'shippers'
        verbose_name = 'shippers'
        verbose_name_plural = 'shippers'

    def __str__(self):
        return self.company_name
