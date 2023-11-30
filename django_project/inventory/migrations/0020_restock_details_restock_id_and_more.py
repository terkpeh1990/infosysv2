# Generated by Django 4.1.10 on 2023-07-25 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_alter_restock_details_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='restock_details',
            name='restock_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='inventory.restocks'),
        ),
        migrations.AlterModelTable(
            name='restock_details',
            table='Restock_detail',
        ),
    ]