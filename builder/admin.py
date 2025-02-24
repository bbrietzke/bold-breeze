from django.contrib import admin
from .models import *

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'tonnage', 'unit_role', 'rules_level', 'date_introduced', 'point_value', 'battle_value')
    ordering = ('name',)

@admin.register(UnitRole)
class UnitRoleAdmin(admin.ModelAdmin):
    list_display = ('role',)
    ordering = ('role',)

@admin.register(Era)
class EraAdmin(admin.ModelAdmin):
    list_display = ('era',)
    ordering = ('era',)

@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    ordering = ('type',)

@admin.register(RulesLevel)
class RulesLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    ordering = ('level',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)