# Generated by Django 4.1.10 on 2023-09-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0013_accountledger_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountledger',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('In Active', 'In Active')], default='In Activate', max_length=50),
        ),
    ]
