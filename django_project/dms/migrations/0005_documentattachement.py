# Generated by Django 4.1.10 on 2023-09-07 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0004_remove_documentdestination_from_unit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentattachement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('document_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachment', to='dms.document')),
            ],
            options={
                'verbose_name': ' Documentattachement',
                'verbose_name_plural': ' Documentattachement',
                'db_table': ' Documentattachements',
            },
        ),
    ]
