# Generated by Django 4.1.10 on 2023-07-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_historicaluser_staffid_user_staffid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='staffid',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='staffid',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
