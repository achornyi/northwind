# Generated by Django 3.1.2 on 2020-10-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]