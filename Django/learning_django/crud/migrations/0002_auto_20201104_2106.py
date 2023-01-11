# Generated by Django 3.0.8 on 2020-11-04 16:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_info',
            name='cv',
        ),
        migrations.AddField(
            model_name='personal_info',
            name='upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='personal_info',
            table='personal_info',
        ),
    ]
