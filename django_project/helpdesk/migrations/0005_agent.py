# Generated by Django 4.1.6 on 2024-04-09 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdesk', '0004_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agentlevel', to='helpdesk.teams')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agentteam', to='helpdesk.teams')),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
                'db_table': 'Agent',
                'managed': True,
            },
        ),
    ]