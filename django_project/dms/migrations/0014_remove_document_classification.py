# Generated by Django 4.1.10 on 2023-09-07 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0013_remove_document_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='classification',
        ),
    ]