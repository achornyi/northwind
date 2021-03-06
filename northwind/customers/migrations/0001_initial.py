# Generated by Django 3.1.2 on 2020-10-27 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDemographics',
            fields=[
                ('customer_type_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('customer_desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'customer_demographics',
                'verbose_name_plural': 'customer_demographics',
                'db_table': 'customer_demographics',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=40)),
                ('contact_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_title', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('region', models.CharField(blank=True, max_length=15, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('phone', models.CharField(blank=True, max_length=24, null=True)),
                ('fax', models.CharField(blank=True, max_length=24, null=True)),
            ],
            options={
                'verbose_name': 'customers',
                'verbose_name_plural': 'customers',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='CustomerCustomerDemo',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='customers.customers')),
                ('customer_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customerdemographics')),
            ],
            options={
                'verbose_name': 'customer_customer_demo',
                'verbose_name_plural': 'customer_customer_demo',
                'db_table': 'customer_customer_demo',
                'unique_together': {('customer', 'customer_type')},
            },
        ),
    ]
