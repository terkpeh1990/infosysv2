# Generated by Django 4.1.10 on 2023-09-11 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicians',
            name='team',
        ),
        migrations.RemoveField(
            model_name='technicians',
            name='technician',
        ),
        migrations.RemoveField(
            model_name='technicians',
            name='tenant_id',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
        migrations.DeleteModel(
            name='Technicians',
        ),
    ]
