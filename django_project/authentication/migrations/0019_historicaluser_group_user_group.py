# Generated by Django 4.1.10 on 2023-07-16 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0018_remove_historicaluser_status_remove_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='group',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.group'),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='auth.group'),
        ),
    ]
