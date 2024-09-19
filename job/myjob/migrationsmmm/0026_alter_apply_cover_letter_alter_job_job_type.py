# Generated by Django 4.2.4 on 2023-09-15 07:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myjob', '0025_remove_job_job_type_ar_remove_job_job_type_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='cover_letter',
            field=ckeditor.fields.RichTextField(verbose_name='cover letter'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Partly time', 'Partly time'), ('Fully time', 'Fully time')], max_length=40, verbose_name='job type'),
        ),
    ]
