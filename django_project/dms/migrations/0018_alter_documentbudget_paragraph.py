# Generated by Django 4.1.10 on 2023-09-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0017_alter_documentbudget_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentbudget',
            name='paragraph',
            field=models.TextField(max_length=1024),
        ),
    ]
