# Generated by Django 4.1.10 on 2023-10-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0047_paymentvoucherbeneficiary_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentvoucherbeneficiary',
            name='comfirm',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]