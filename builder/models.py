from django.db import models

class RulesLevel(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class UnitType(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class UnitRole(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Era(models.Model):
    name = models.CharField(max_length=128, unique=True)
    master_unit_list_id = models.PositiveSmallIntegerField(default=0, unique=True)
    slug = models.CharField(max_length=64, unique=True)
    start = models.PositiveSmallIntegerField(default=0, unique=True)
    end = models.PositiveSmallIntegerField(default=0, unique=True)

    def __str__(self):
        return "{0} from {1} to {2} ( {3} )".format(self.name, self.start, self.end, self.slug)
    
class Faction(models.Model):
    name = models.CharField(max_length=128, unique=True)
    master_unit_list_id = models.PositiveSmallIntegerField(default=0, unique=True)
    slug = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    
class Technology(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=128, unique=False)
    slug = models.CharField(max_length=64, unique=True)
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

