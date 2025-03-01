# Generated by Django 5.1.6 on 2025-02-24 00:43

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
                ('era', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RulesLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tonnage', models.PositiveSmallIntegerField(default=0)),
                ('battle_value', models.PositiveSmallIntegerField(default=0)),
                ('cost', models.PositiveBigIntegerField(default=0)),
                ('date_introduced', models.PositiveBigIntegerField(default=0)),
                ('notes', models.TextField(max_length=500)),
                ('point_value', models.PositiveSmallIntegerField(default=0)),
                ('master_unit_list_number', models.PositiveSmallIntegerField(default=0, unique=True)),
                ('era', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='builder.era')),
                ('rules_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='builder.ruleslevel')),
                ('technology', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='builder.technology')),
                ('unit_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='builder.unitrole')),
                ('unit_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='builder.unittype')),
            ],
        ),
    ]
