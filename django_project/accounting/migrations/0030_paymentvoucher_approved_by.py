# Generated by Django 4.1.10 on 2023-10-05 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting', '0029_paymentvoucher_authorized_and_passed_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentvoucher',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pvapprovedby', to=settings.AUTH_USER_MODEL),
        ),
    ]