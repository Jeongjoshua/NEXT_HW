# Generated by Django 5.0.4 on 2024-04-04 08:58

import pytz.tzinfo
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_post_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='due_date',
            field=models.DateTimeField(default=pytz.tzinfo.DstTzInfo.localize),
        ),
    ]
