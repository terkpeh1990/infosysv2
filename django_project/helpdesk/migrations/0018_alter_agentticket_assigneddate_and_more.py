# Generated by Django 4.1.6 on 2024-04-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0017_alter_agentticket_assigneddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentticket',
            name='assigneddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agentticket',
            name='completeddate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
