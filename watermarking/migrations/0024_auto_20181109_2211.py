# Generated by Django 2.0 on 2018-11-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermarking', '0023_watermarkimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watermarkimage',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
