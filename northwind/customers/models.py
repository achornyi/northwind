from django.db import models


# Create your models here.
class Customers(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=10)
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
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.customer_id

    class Meta:
        db_table = 'customers'
        verbose_name = 'customers'
        verbose_name_plural = 'customers'


class CustomerCustomerDemo(models.Model):
    customer = models.OneToOneField('Customers', models.DO_NOTHING, primary_key=True)
    customer_type = models.ForeignKey('CustomerDemographics', models.DO_NOTHING)

    class Meta:
        db_table = 'customer_customer_demo'
        unique_together = (('customer', 'customer_type'),)
        verbose_name = 'customer demo'
        verbose_name_plural = 'customer demo'


class CustomerDemographics(models.Model):
    customer_type_id = models.CharField(primary_key=True, max_length=10)
    customer_desc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'customer_demographics'
        verbose_name = 'customer demographics'
        verbose_name_plural = 'customer demographics'
