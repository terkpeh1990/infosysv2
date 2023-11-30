# Generated by Django 4.1.10 on 2023-10-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0041_documentbeneficiary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentbeneficiary',
            name='amount_received',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]