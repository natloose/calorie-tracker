# Generated by Django 3.1.3 on 2020-11-26 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201126_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userconsumption',
            name='fiber',
        ),
    ]
