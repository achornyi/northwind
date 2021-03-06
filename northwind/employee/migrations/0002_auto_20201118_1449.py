# Generated by Django 3.1.2 on 2020-11-18 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeterritories',
            options={'verbose_name': 'employee territories', 'verbose_name_plural': 'employee territories'},
        ),
        migrations.AlterModelOptions(
            name='usstates',
            options={'verbose_name': 'us states', 'verbose_name_plural': 'us states'},
        ),
        migrations.AddField(
            model_name='employees',
            name='territories',
            field=models.ManyToManyField(through='employee.EmployeeTerritories', to='employee.Territories'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employeeterritories',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='employee.employees'),
        ),
        migrations.AlterField(
            model_name='employeeterritories',
            name='territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.territories'),
        ),
    ]
