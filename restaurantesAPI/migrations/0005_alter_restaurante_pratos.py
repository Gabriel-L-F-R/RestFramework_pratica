# Generated by Django 5.1.1 on 2024-09-19 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantesAPI', '0004_alter_restaurante_pratos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='pratos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantesAPI.pratos'),
        ),
    ]
