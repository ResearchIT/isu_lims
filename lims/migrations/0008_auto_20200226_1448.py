# Generated by Django 3.0.3 on 2020-02-26 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0007_auto_20200226_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accession',
            old_name='genusflat',
            new_name='genus',
        ),
        migrations.RenameField(
            model_name='accession',
            old_name='subgenusflat',
            new_name='subgenus',
        ),
        migrations.RenameField(
            model_name='accession',
            old_name='genomeflat',
            new_name='genome',
        ),
        migrations.RenameField(
            model_name='accession',
            old_name='speciesflat',
            new_name='species',
        ),
    ]