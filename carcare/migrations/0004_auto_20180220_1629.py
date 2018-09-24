# Generated by Django 2.0.2 on 2018-02-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carcare', '0003_remove_service_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='tire_size',
            field=models.CharField(default='16inch', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='vin',
            field=models.CharField(default='VIN Number', max_length=17),
            preserve_default=False,
        ),
    ]