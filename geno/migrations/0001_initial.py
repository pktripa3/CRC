# Generated by Django 5.0 on 2023-12-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genome_crc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_id', models.IntegerField()),
                ('Org_name', models.TextField()),
                ('GeneID', models.IntegerField()),
                ('CurrentID', models.IntegerField()),
                ('Status', models.TextField()),
                ('Symbol', models.TextField()),
                ('Aliases', models.TextField()),
                ('description', models.TextField()),
                ('other_designations', models.TextField()),
                ('map_location', models.IntegerField()),
                ('chromosome', models.TextField()),
                ('genomic_nucleotide_accession', models.TextField()),
                ('start_position_on_the_genomic_accession', models.IntegerField()),
                ('end_position_on_the_genomic_accession', models.IntegerField()),
                ('orientation', models.TextField()),
                ('exon_count', models.IntegerField()),
                ('OMIM', models.IntegerField()),
            ],
        ),
    ]
