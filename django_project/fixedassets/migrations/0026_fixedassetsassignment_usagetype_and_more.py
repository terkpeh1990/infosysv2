# Generated by Django 4.1.6 on 2024-03-20 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fixedassets', '0025_fixedasset_user_alter_fixedasset_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedassetsassignment',
            name='usagetype',
            field=models.CharField(choices=[('Pool', 'Pool'), ('Assigned', 'Assigned')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fixedasset',
            name='currentstatus',
            field=models.CharField(choices=[('In Use', 'In Use'), ('Not in Use', 'Not in Use'), ('Retired', 'Retired'), ('Disposed', 'Disposed'), ('On-going', 'On-going'), ('Abandoned', 'Abandoned'), ('Suspended', 'Suspended'), ('Assigned', 'Assigned'), ('Avialable', 'Avialable')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fixedassetsassignment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignedto', to=settings.AUTH_USER_MODEL),
        ),
    ]
