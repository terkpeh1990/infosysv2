# Generated by Django 4.1.6 on 2024-04-09 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0006_agent_costcenter_agent_subcostcenter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'managed': True, 'permissions': [('custom_create_agent', 'Can Create Helpdesk Agent')], 'verbose_name': 'Agent', 'verbose_name_plural': 'Agents'},
        ),
    ]
