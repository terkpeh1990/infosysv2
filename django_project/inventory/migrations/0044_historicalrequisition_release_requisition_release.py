# Generated by Django 4.1.10 on 2023-07-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0043_alter_historicalrequisition_details_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrequisition',
            name='release',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requisition',
            name='release',
            field=models.BooleanField(default=False),
        ),
    ]
