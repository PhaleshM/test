# Generated by Django 4.0.3 on 2023-03-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0005_rename_user_listingimage_name_alter_listing_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='product',
            field=models.CharField(choices=[('Harvester', 'Harvester'), ('Plough', 'Plough'), ('Rotavator', 'Rotavator'), ('Tractor', 'Tractor'), ('Seed Drill', 'Seed_Drill'), ('Sprayer', 'Sprayer'), ('Trailer', 'Trailer'), ('Cultivator', 'Cultivator'), ('Baler', 'Baler')], max_length=50),
        ),
    ]
