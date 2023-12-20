# Generated by Django 4.1.6 on 2023-12-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0025_user_hq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalgrade',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Rank'},
        ),
        migrations.AlterField(
            model_name='historicalgrade',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]
