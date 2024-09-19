from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.db.models import Count

JOB_TYPE = (
    ('Partly time', _('Partly time')),
    ('Fully time', _('Fully time')),
)

class Job(models.Model):
    # Step 1
    tags=TaggableManager()
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE, verbose_name=_('owner'))
    title_ar = models.CharField(max_length=33, verbose_name=_('title (Arabic)'))
    location_ar = models.CharField(max_length=80, verbose_name=_('location (Arabic)'))
    description_ar = RichTextField(verbose_name=_('description (Arabic)'))
    # Step 2
    title_en = models.CharField(max_length=33, verbose_name=_('title (English)'))
    location_en = models.CharField(max_length=80, verbose_name=_('location (English)'))
    description_en = RichTextField(verbose_name=_('description (English)'))

    job_type= models.CharField(max_length=40, choices=JOB_TYPE, verbose_name=_('job type'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE,null=True, verbose_name=_('category'))
    vacancy = models.IntegerField(default=1, verbose_name=_('vacancy'))
    salary = models.IntegerField(default=0, verbose_name=_('salary'))
    experience = models.IntegerField(default=1, verbose_name=_('experience'))
    image = models.ImageField(null=True, blank=True, upload_to="images/%Y-%m-%d", verbose_name=_('image'))
    published_at = models.DateTimeField(auto_now=True, verbose_name=_('published at'))
    available = models.BooleanField(default=True, verbose_name=_('available'))

    slug = models.SlugField(blank=True, null=True, verbose_name=_('slug'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_en)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title_en

class Category(models.Model):
    name_en = models.CharField(max_length=44, verbose_name=_('name (English)'))
    name_ar = models.CharField(max_length=44, verbose_name=_('name (Arabic)'))

    def __str__(self):
        return self.name_en

from django.core.validators import FileExtensionValidator

class Apply(models.Model):
    Applier = models.ForeignKey(User, related_name='job_applier', on_delete=models.CASCADE, verbose_name=_('Applier'))
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE, verbose_name=_('job'))
    email = models.EmailField(max_length=88, verbose_name=_('email'))
    website = models.URLField(verbose_name=_('website'))
    cv = models.FileField(upload_to='apply/', verbose_name=_('cv'), validators=[FileExtensionValidator(['pdf'], message='Please upload a PDF file.')])
    cover_letter = models.TextField(verbose_name=_('cover letter'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.Applier = User.objects.get(pk=self.Applier_id)  # Set Applier as the currently logged-in user
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.Applier.username


from django.contrib.auth import get_user_model
User = get_user_model()
class Comment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, related_name='commented_name', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['created']),]

    def __str__(self):
        return f'Comment by {self.name} on {self.job}'

    @property
    def email(self):
        return self.name.email

