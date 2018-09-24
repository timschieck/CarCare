# Generated by Django 2.0.2 on 2018-02-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carcare', '0006_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='notes',
            field=models.TextField(default='Replaced all four tires at DiscountTire'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
