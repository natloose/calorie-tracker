# Generated by Django 3.1.3 on 2020-11-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20201129_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconsumption',
            name='protein',
            field=models.IntegerField(default=None),
        ),
    ]
