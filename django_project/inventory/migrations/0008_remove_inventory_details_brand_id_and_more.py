# Generated by Django 4.1.10 on 2023-07-19 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_inventory_brand_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory_details',
            name='brand_id',
        ),
        migrations.RemoveField(
            model_name='inventory_details',
            name='category_id',
        ),
    ]