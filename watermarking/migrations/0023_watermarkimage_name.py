# Generated by Django 2.0 on 2018-11-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermarking', '0022_auto_20181109_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='watermarkimage',
            name='name',
            field=models.CharField(default='Name', max_length=128, unique=True),
        ),
    ]
