# Generated by Django 3.2.8 on 2021-11-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211029_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listed_Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('list_car_name', models.CharField(max_length=200)),
                ('list_price', models.IntegerField()),
                ('list_km_driven', models.IntegerField()),
                ('list_owners_count', models.IntegerField()),
                ('list_year', models.IntegerField()),
                ('list_fuel_type', models.CharField(max_length=200)),
                ('list_transmission_type', models.CharField(max_length=200)),
                ('list_phone_number', models.IntegerField()),
                ('list_seller_name', models.CharField(max_length=200)),
                ('list_city', models.CharField(max_length=200)),
                ('list_number_plate', models.CharField(max_length=200)),
            ],
        ),
    ]
