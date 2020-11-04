from django.db import models


# Create your models here.
class Region(models.Model):
    region_id = models.SmallIntegerField(primary_key=True)
    region_description = models.CharField(max_length=50)

    def __str__(self):
        return self.region_description

    class Meta:
        db_table = 'region'


class Territories(models.Model):
    territory_id = models.CharField(primary_key=True, max_length=20)
    territory_description = models.CharField(max_length=50)
    region = models.ForeignKey(Region, models.DO_NOTHING)

    def __str__(self):
        return self.territory_description

    class Meta:
        db_table = 'territories'
        verbose_name = 'territories'
        verbose_name_plural = 'territories'


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
    territories = models.ManyToManyField(Territories, through='EmployeeTerritories')
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
        verbose_name = 'employees'
        verbose_name_plural = 'employees'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UsStates(models.Model):
    state_id = models.SmallIntegerField(primary_key=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    state_abbr = models.CharField(max_length=2, blank=True, null=True)
    state_region = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = 'us_states'
        verbose_name = 'us states'
        verbose_name_plural = 'us states'


class EmployeeTerritories(models.Model):
    employee = models.OneToOneField(Employees, on_delete=models.CASCADE, primary_key=True)
    territory = models.ForeignKey(Territories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee_territories'
        unique_together = (('employee', 'territory'),)
        verbose_name = 'employee territories'
        verbose_name_plural = 'employee territories'
