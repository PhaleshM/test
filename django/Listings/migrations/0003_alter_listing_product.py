# Generated by Django 4.0.3 on 2023-03-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0002_rename_discription_listing_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='product',
            field=models.CharField(choices=[('Seed Drill', 'Seed_Drill'), ('Sprayer', 'Sprayer'), ('Tractor', 'Tractor'), ('Trailer', 'Trailer'), ('Baler', 'Baler'), ('Harvester', 'Harvester'), ('Plough', 'Plough'), ('Rotavator', 'Rotavator'), ('Cultivator', 'Cultivator')], max_length=50),
        ),
    ]
