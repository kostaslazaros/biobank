# Generated by Django 4.1.7 on 2023-03-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0002_remove_dataset_username_dataset_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='disease',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dataset.disease'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='modality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dataset.modality'),
            preserve_default=False,
        ),
    ]
