# Generated by Django 2.0.2 on 2018-07-15 18:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 15, 18, 4, 49, 684913, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
