# Generated by Django 2.0.2 on 2018-02-17 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=0)),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('license_plate', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('miles', models.IntegerField(default=0)),
                ('trim_package', models.CharField(max_length=50)),
                ('engine', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date added')),
                ('gallons', models.DecimalField(decimal_places=3, max_digits=5)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carcare.Car')),
            ],
        ),
    ]