# Generated by Django 4.1.10 on 2023-10-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0041_alter_paymentvoucher_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payables',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
