# Generated by Django 4.2.4 on 2023-09-09 18:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myjob', '0022_alter_myjob_description_ar_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myjob',
            new_name='Job',
        ),
    ]
