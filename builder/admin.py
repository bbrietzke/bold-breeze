from django.contrib import admin
from .models import *

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'tonnage', 'unit_role', 'rules_level', 'date_introduced', 'point_value', 'battle_value')
    ordering = ('name',)

@admin.register(Technology)
@admin.register(RulesLevel)
@admin.register(UnitType)
@admin.register(Era)
@admin.register(UnitRole)
@admin.register(Faction)
class LookupTableAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)