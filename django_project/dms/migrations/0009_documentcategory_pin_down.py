# Generated by Django 4.1.10 on 2023-09-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0008_documentcategory_can_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentcategory',
            name='pin_down',
            field=models.BooleanField(default=False),
        ),
    ]