# Generated by Django 2.0 on 2018-10-19 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('watermarking', '0004_auto_20181019_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watermarking',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 19, 15, 37, 44, 648163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='watermarking',
            name='paper',
            field=models.FileField(blank=True, upload_to='paper/'),
        ),
        migrations.AlterField(
            model_name='watermarking',
            name='source_code',
            field=models.FileField(blank=True, upload_to='source_code/'),
        ),
    ]
