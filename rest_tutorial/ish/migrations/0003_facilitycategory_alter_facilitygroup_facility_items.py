# Generated by Django 4.2 on 2023-04-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ish', '0002_facilitygroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='facilitygroup',
            name='facility_items',
            field=models.ManyToManyField(blank=True, to='ish.facilityitem'),
        ),
    ]
