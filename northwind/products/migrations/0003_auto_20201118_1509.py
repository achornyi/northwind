# Generated by Django 3.1.2 on 2020-11-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201118_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shippers',
            name='shipper_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='supplier_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]