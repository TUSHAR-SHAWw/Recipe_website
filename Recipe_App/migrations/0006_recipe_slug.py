# Generated by Django 4.2.7 on 2023-12-09 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_App', '0005_report_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 12, 9, 7, 45, 20, 747017, tzinfo=datetime.timezone.utc), unique=True),
            preserve_default=False,
        ),
    ]