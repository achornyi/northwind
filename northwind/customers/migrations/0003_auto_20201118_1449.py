# Generated by Django 3.1.2 on 2020-11-18 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customers_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customercustomerdemo',
            options={'verbose_name': 'customer demo', 'verbose_name_plural': 'customer demo'},
        ),
        migrations.AlterModelOptions(
            name='customerdemographics',
            options={'verbose_name': 'customer demographics', 'verbose_name_plural': 'customer demographics'},
        ),
    ]
