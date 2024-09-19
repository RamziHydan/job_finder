# Generated by Django 4.2.4 on 2023-08-20 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myjob', '0011_myjob_onwer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='name',
        ),
        migrations.AddField(
            model_name='apply',
            name='Applier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job_applier', to=settings.AUTH_USER_MODEL),
        ),
    ]
