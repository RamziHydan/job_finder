# Generated by Django 4.2.4 on 2023-09-09 12:20

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myjob', '0018_alter_apply_cover_letter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100)),
                ('name_fr', models.CharField(max_length=100)),
                ('school_en', models.CharField(max_length=100)),
                ('school_fr', models.CharField(max_length=100)),
                ('city_en', models.CharField(max_length=100)),
                ('city_fr', models.CharField(max_length=100)),
                ('major_en', models.CharField(max_length=100)),
                ('major_fr', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='apply',
            name='Applier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applier', to=settings.AUTH_USER_MODEL, verbose_name='Applier'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='cover_letter',
            field=ckeditor.fields.RichTextField(verbose_name='cover_letter'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='cv',
            field=models.FileField(upload_to='apply/', verbose_name='cv'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='email',
            field=models.EmailField(max_length=88, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='myjob.myjob', verbose_name='job'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='website',
            field=models.URLField(verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=44, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='available',
            field=models.BooleanField(default=True, verbose_name='available'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myjob.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='experience',
            field=models.IntegerField(default=1, verbose_name='experience'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y-%m-%d', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='job_type',
            field=models.CharField(choices=[('Prtlay Time', 'Prtlay Time'), ('Fully Time', 'Fully Time')], max_length=40, verbose_name='job_type'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='location',
            field=models.CharField(max_length=80, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='published_at',
            field=models.DateTimeField(auto_now=True, verbose_name='published_at'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='salary',
            field=models.IntegerField(default=0, verbose_name='salary'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='title',
            field=models.CharField(max_length=33, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='myjob',
            name='vacancy',
            field=models.IntegerField(default=1, verbose_name='vacancy'),
        ),
    ]
