# Generated by Django 5.0 on 2023-12-31 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fam_crc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant_common_name', models.TextField()),
                ('Scientific_Name', models.TextField()),
                ('Family', models.TextField()),
            ],
        ),
    ]
