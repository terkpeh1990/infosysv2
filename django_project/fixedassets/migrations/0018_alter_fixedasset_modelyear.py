# Generated by Django 4.1.6 on 2024-03-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixedassets', '0017_fixedasset_chassisno_fixedasset_colour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedasset',
            name='modelyear',
            field=models.IntegerField(null=True),
        ),
    ]
