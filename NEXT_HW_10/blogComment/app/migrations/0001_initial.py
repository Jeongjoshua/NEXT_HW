# Generated by Django 5.0.4 on 2024-04-10 05:59

import pytz.tzinfo
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('hobby', 'Hobby'), ('food', 'Food'), ('programming', 'Programming')], default='hobby', max_length=20)),
                ('published_date', models.DateTimeField(default=pytz.tzinfo.DstTzInfo.localize)),
            ],
        ),
    ]
