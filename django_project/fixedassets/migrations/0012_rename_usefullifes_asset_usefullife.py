# Generated by Django 4.1.6 on 2024-03-09 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixedassets', '0011_rename_usefullife_asset_usefullifes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='usefullifes',
            new_name='usefullife',
        ),
    ]
