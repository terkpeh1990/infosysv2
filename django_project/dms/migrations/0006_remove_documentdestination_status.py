# Generated by Django 4.1.10 on 2023-09-07 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0005_documentattachement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentdestination',
            name='status',
        ),
    ]