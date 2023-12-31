# Generated by Django 5.0 on 2023-12-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metabolite_crc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant_Name', models.CharField(max_length=100)),
                ('Metabolites', models.CharField(max_length=100)),
                ('Pathway', models.TextField()),
                ('References', models.URLField()),
                ('Citation', models.TextField()),
            ],
        ),
    ]