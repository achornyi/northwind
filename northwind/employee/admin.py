from django.contrib import admin

from .models import Employees, EmployeeTerritories, Region, Territories, UsStates


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id',
        'last_name',
        'first_name',
        'title',
        'title_of_courtesy',
        'birth_date',
        'hire_date',
        'address',
        'city',
        'region',
        'postal_code',
        'country',
        'home_phone',
        'extension',
        'photo',
        'notes',
        'reports_to',
        'photo_path',
    )
    list_filter = ('birth_date', 'hire_date', 'reports_to')


@admin.register(EmployeeTerritories)
class EmployeeTerritoriesAdmin(admin.ModelAdmin):
    list_display = ('employee', 'territory')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_id', 'region_description')


@admin.register(Territories)
class TerritoriesAdmin(admin.ModelAdmin):
    list_display = ('territory_id', 'territory_description', 'region')


@admin.register(UsStates)
class UsStatesAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'state_name', 'state_abbr', 'state_region')

