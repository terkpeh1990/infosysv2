# Generated by Django 4.1.10 on 2023-07-16 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_alter_historicaluser_password_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaluser',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
