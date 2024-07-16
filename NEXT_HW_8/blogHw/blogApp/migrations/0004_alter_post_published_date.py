# Generated by Django 5.0.3 on 2024-04-03 02:34

import pytz.tzinfo
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=pytz.tzinfo.DstTzInfo.localize),
        ),
    ]
