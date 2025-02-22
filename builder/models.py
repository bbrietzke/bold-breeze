from django.db import models

class RulesLevel(models.Model):
    level = models.CharField(max_length=50)

class UnitType(models.Model):
    type = models.CharField(max_length=20)

class UnitRole(models.Model):
    role = models.CharField(max_length=20)

class Era(models.Model):
    era = models.CharField(max_length=20)

class Unit(models.Model):
    name = models.CharField(max_length=50)
    tonnage = models.PositiveSmallIntegerField(default=0)
    battle_value = models.PositiveSmallIntegerField(default=0)
    cost = models.PositiveBigIntegerField(default=0)
    rules_level = models.ForeignKey(RulesLevel, on_delete=models.PROTECT)
    unit_type = models.ForeignKey(UnitType, on_delete=models.PROTECT)
    unit_role = models.ForeignKey(UnitRole, on_delete=models.PROTECT)
    data_introduced = models.PositiveBigIntegerField(default=0)
    era = models.ForeignKey(Era, on_delete=models.PROTECT)
    notes =  models.CharField(max_length=200)
    point_value = models.PositiveSmallIntegerField(default=0)
    master_unit_list_number = models.PositiveSmallIntegerField(default=0)
