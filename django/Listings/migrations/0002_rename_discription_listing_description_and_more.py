# Generated by Django 4.0.3 on 2023-03-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='discription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='listing',
            name='product',
            field=models.CharField(choices=[('Tractor', 'Tractor'), ('Seed Drill', 'Seed_Drill'), ('Cultivator', 'Cultivator'), ('Sprayer', 'Sprayer'), ('Plough', 'Plough'), ('Rotavator', 'Rotavator'), ('Baler', 'Baler'), ('Harvester', 'Harvester'), ('Trailer', 'Trailer')], max_length=50),
        ),
        migrations.AlterField(
            model_name='listing',
            name='ratecriteria',
            field=models.IntegerField(choices=[('2', 'per day'), ('1', 'per hour'), ('3', 'per Km')]),
        ),
    ]
