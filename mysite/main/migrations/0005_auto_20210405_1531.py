# Generated by Django 2.1.5 on 2021-04-05 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210325_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 15, 31, 53, 434382), verbose_name='date published'),
        ),
    ]