# Generated by Django 5.0.1 on 2024-01-18 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoinment', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appoinment.appointment'),
        ),
    ]
