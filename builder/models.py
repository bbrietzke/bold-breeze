from django.db import models
from django.contrib import admin

class RulesLevel(models.Model):
    level = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.level

class UnitType(models.Model):
    type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.type

class UnitRole(models.Model):
    role = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.role

class Era(models.Model):
    era = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.era
    
class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=60, unique=False)
    tonnage = models.PositiveSmallIntegerField(default=0)
    battle_value = models.PositiveSmallIntegerField(default=0)
    cost = models.PositiveBigIntegerField(default=0)
    rules_level = models.ForeignKey(RulesLevel, on_delete=models.PROTECT)
    unit_type = models.ForeignKey(UnitType, on_delete=models.PROTECT, null=True)
    unit_role = models.ForeignKey(UnitRole, on_delete=models.PROTECT)
    date_introduced = models.PositiveBigIntegerField(default=0)
    era = models.ForeignKey(Era, on_delete=models.PROTECT, null=True)
    notes =  models.TextField(max_length=500)
    point_value = models.PositiveSmallIntegerField(default=0)
    master_unit_list_number = models.PositiveSmallIntegerField(default=0, unique=True)
    technology = models.ForeignKey(Technology, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return "{0}".format(self.name)

