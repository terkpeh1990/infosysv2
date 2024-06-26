# Generated by Django 4.1.6 on 2024-03-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixedassets', '0021_remove_historicalsubcategory_classification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedasset',
            name='tagno',
            field=models.CharField(error_messages={'unique': 'Asset With this Chassis/Serial number already exist.'}, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='fixedasset',
            name='chassisno',
            field=models.CharField(error_messages={'unique': 'Asset With this Chassis/Serial number already exist.'}, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='fixedasset',
            name='engineserialno',
            field=models.CharField(error_messages={'unique': 'Asset With this Tag number already exist.'}, max_length=255, null=True, unique=True),
        ),
    ]
