# Generated by Django 4.1.10 on 2023-07-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_historicaluser_grade_user_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]