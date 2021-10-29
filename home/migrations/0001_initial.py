# Generated by Django 3.2.8 on 2021-10-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('selling_price', models.CharField(max_length=200)),
                ('present_price', models.CharField(max_length=200)),
                ('kms_driven', models.CharField(max_length=200)),
                ('fuel_type', models.CharField(max_length=200)),
                ('seller_type', models.CharField(max_length=200)),
                ('transmission', models.CharField(max_length=200)),
                ('owners', models.CharField(max_length=200)),
            ],
        ),
    ]