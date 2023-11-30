# Generated by Django 4.1.10 on 2023-07-27 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0035_alter_requisition_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisition',
            options={'permissions': [('custom_create_requisition', 'Can Create Requisition'), ('custom_update_requisition', 'Can Update Requisition'), ('custom_delete_requisition', 'Can Delete Requisition'), ('custom_view_requisition', 'Can View Requisition'), ('custom_approve_requisition', 'Can Approve Requisition'), ('custom_approve_capital_requisition', 'Administration Can Approve Capital Requisition'), ('custom_approve_consumable_requisition', 'Administration Can Approve Consumable Requisition')], 'verbose_name': 'Requisition', 'verbose_name_plural': 'Requisitions'},
        ),
        migrations.RemoveField(
            model_name='historicalrequisition_details',
            name='done',
        ),
        migrations.RemoveField(
            model_name='requisition_details',
            name='done',
        ),
    ]
