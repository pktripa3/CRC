# Generated by Django 5.0 on 2024-01-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NaturalDrug', '0002_alter_drug_crc_drug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug_crc',
            name='Drug_ID_MESH',
            field=models.CharField(max_length=200),
        ),
    ]