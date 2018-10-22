# Generated by Django 2.0 on 2018-10-19 20:00

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('watermarking', '0008_auto_20181019_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watermarking',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 19, 20, 0, 29, 906911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='watermarking',
            name='paper',
            field=models.FileField(blank=True, upload_to='paper/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'], message="Please upload '.pdf' files only.")]),
        ),
        migrations.AlterField(
            model_name='watermarking',
            name='source_code',
            field=models.FileField(blank=True, upload_to='source_code/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['py'], message="Please upload '.py' files only.")]),
        ),
    ]
