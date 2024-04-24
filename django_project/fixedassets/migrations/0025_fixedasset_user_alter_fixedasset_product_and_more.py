# Generated by Django 4.1.6 on 2024-03-20 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0069_remove_job_certification_lpo_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0008_remove_devision_location'),
        ('fixedassets', '0024_fixedasset_costbf_fixedasset_costcf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedasset',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currentuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fixedasset',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fixedassetproduct', to='inventory.products'),
        ),
        migrations.CreateModel(
            name='FixedAssetsAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigndate', models.DateField(null=True)),
                ('returndate', models.DateField(null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixedasset', to='fixedassets.fixedasset')),
                ('costcenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigntocostcenter', to='company.devision')),
                ('subcostcenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigntoubcostcenter', to='company.sub_devision')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignedto', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FixedAssetsAssignment',
                'verbose_name_plural': 'FixedAssetsAssignments',
                'db_table': 'FixedAssetsAssignments',
            },
        ),
    ]
