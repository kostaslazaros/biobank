# Generated by Django 4.1.7 on 2023-03-31 11:07

import dataset.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0004_dataset_measurable_index_dataset_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='zipfile',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=dataset.models.Dataset.file_upload_to),
        ),
    ]
