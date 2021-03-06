# Generated by Django 3.1.3 on 2020-11-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201126_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconsumption',
            name='calories',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userconsumption',
            name='carbohydrates',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userconsumption',
            name='fat',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userconsumption',
            name='fiber',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userconsumption',
            name='food',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userconsumption',
            name='protein',
            field=models.IntegerField(default=1),
        ),
    ]
