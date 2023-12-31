# Generated by Django 4.1.10 on 2023-10-24 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0054_imprest_notify_alter_imprest_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imprest',
            options={'permissions': [('custom_create_imprest', 'Can Create Imprest'), ('custom_approve_imprest', 'Can Approve Imprest'), ('custom_certify_imprest', 'Can Certify Imprest'), ('custom_pay_imprest', 'Can Pay Imprest'), ('custom_district', 'Can Generate Imprest at District Level '), ('custom_region', 'Can Generate Imprest at Regional Level'), ('custom_hq', 'Can Generate Imprest at Hq Level')], 'verbose_name': 'Imprest', 'verbose_name_plural': 'Imprests'},
        ),
    ]
