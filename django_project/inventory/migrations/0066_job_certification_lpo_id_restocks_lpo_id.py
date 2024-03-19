# Generated by Django 4.1.6 on 2024-02-02 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0011_rename_purchase_requisition_date_localpurchasingorder_lpo_date'),
        ('inventory', '0065_alter_job_detail_funding'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_certification',
            name='lpo_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_lpo', to='purchase_order.localpurchasingorder'),
        ),
        migrations.AddField(
            model_name='restocks',
            name='lpo_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restock_lpo', to='purchase_order.localpurchasingorder'),
        ),
    ]