from django.db import models


# Create your models here.
class Employees(models.Model):
    employee_id = models.SmallIntegerField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    title_of_courtesy = models.CharField(max_length=25, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    home_phone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reports_to', blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'employees'


class EmployeeTerritories(models.Model):
    employee = models.OneToOneField('Employees', models.DO_NOTHING, primary_key=True)
    territory = models.ForeignKey('Territories', models.DO_NOTHING)

    class Meta:
        db_table = 'employee_territories'
        unique_together = (('employee', 'territory'),)


class Region(models.Model):
    region_id = models.SmallIntegerField(primary_key=True)
    region_description = models.CharField(max_length=50)

    class Meta:
        db_table = 'region'


class Territories(models.Model):
    territory_id = models.CharField(primary_key=True, max_length=20)
    territory_description = models.CharField(max_length=50)
    region = models.ForeignKey(Region, models.DO_NOTHING)

    class Meta:
        db_table = 'territories'


class UsStates(models.Model):
    state_id = models.SmallIntegerField(primary_key=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    state_abbr = models.CharField(max_length=2, blank=True, null=True)
    state_region = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'us_states'
