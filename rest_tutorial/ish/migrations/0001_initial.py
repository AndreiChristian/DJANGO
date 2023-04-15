# Generated by Django 4.2 on 2023-04-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('imagePath', models.TextField()),
                ('level', models.CharField(choices=[('G', 'Guest'), ('R', 'Room'), ('P', 'Property')], max_length=2)),
                ('included', models.BooleanField(default=True)),
                ('extraPrice', models.IntegerField(default=0)),
            ],
        ),
    ]