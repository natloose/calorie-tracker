# Generated by Django 3.1.3 on 2020-11-29 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20201127_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconsumption',
            name='datestamp',
            field=models.DateField(default=datetime.date(2020, 11, 29)),
        ),
        migrations.AlterField(
            model_name='userconsumption',
            name='protein',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
