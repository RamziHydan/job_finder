# Generated by Django 4.2.4 on 2023-09-09 15:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myjob', '0021_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myjob',
            name='description_ar',
            field=ckeditor.fields.RichTextField(verbose_name='description (Arabic)'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='description_en',
            field=ckeditor.fields.RichTextField(verbose_name='description (English)'),
        ),
    ]
