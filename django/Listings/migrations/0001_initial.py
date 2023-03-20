# Generated by Django 4.0.3 on 2023-03-18 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product', models.CharField(choices=[('Cultivator', 'Cultivator'), ('Sprayer', 'Sprayer'), ('Trailer', 'Trailer'), ('Plough', 'Plough'), ('Seed Drill', 'Seed_Drill'), ('Rotavator', 'Rotavator'), ('Tractor', 'Tractor'), ('Baler', 'Baler'), ('Harvester', 'Harvester')], max_length=50)),
                ('discription', models.TextField()),
                ('ratecriteria', models.IntegerField(choices=[('1', 'per hour'), ('3', 'per Km'), ('2', 'per day')])),
                ('rate', models.IntegerField()),
                ('slug', models.CharField(max_length=80)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Listings.listing')),
            ],
        ),
    ]