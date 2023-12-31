# Generated by Django 4.1.10 on 2023-10-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0053_impresttimeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='imprest',
            name='notify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='imprest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled'), ('Certified', 'Certified'), ('Paid', 'Paid'), ('Retired', 'Retired')], default='Pending', max_length=60),
        ),
    ]
