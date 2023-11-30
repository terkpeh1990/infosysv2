# Generated by Django 4.1.10 on 2023-07-27 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_alter_requisition_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisition',
            options={'permissions': [('custom_create_requisition', 'Can Create Requisition'), ('custom_update_requisition', 'Can Update Requisition'), ('custom_delete_requisition', 'Can Delete Requisition'), ('custom_view_requisition', 'Can View Requisition'), ('custom_approve_requisition', 'Can Approve Requisition'), ('custom_approve_capital_requisition', 'Administration Can Approve Capital Requisition'), ('custom_approve_consumable_requisition', 'Administration Can Approve Consumable Requisition'), ('custom_issue__requisition', 'Stores Issue Requisition')], 'verbose_name': 'Requisition', 'verbose_name_plural': 'Requisitions'},
        ),
    ]