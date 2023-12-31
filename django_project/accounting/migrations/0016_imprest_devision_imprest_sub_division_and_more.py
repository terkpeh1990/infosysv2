# Generated by Django 4.1.10 on 2023-09-26 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_devision_code_sub_devision_code'),
        ('accounting', '0015_bankaccountstype_paymentvoucher_accountledger_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imprest',
            name='devision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imprestdevisions', to='company.devision'),
        ),
        migrations.AddField(
            model_name='imprest',
            name='sub_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imprestsub_districts', to='company.sub_devision'),
        ),
        migrations.AlterField(
            model_name='paymentvoucher',
            name='type_of_pay',
            field=models.CharField(choices=[('Third Party', 'Third Party'), ('Refund', 'Refund'), ('Accountable Imprest', 'Accountable Imprest')], default='Staff', max_length=100),
        ),
    ]
