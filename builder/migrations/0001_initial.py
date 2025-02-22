# Generated by Django 5.1.6 on 2025-02-22 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Era',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('era', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RulesLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnitRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tonnage', models.PositiveSmallIntegerField(default=0)),
                ('battle_value', models.PositiveSmallIntegerField(default=0)),
                ('cost', models.PositiveBigIntegerField(default=0)),
                ('data_introduced', models.PositiveBigIntegerField(default=0)),
                ('notes', models.CharField(max_length=200)),
                ('point_value', models.PositiveSmallIntegerField(default=0)),
                ('master_unit_list_number', models.PositiveSmallIntegerField(default=0)),
                ('era', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='builder.era')),
                ('rules_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='builder.ruleslevel')),
                ('unit_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='builder.unitrole')),
                ('unit_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='builder.unittype')),
            ],
        ),
    ]
