# Generated by Django 4.1.10 on 2023-09-20 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0031_alter_document_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentattachement',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documentattachmentdestination', to='dms.documentdestination'),
        ),
        migrations.AddField(
            model_name='documentbudget',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documentbudgetdestination', to='dms.documentdestination'),
        ),
    ]