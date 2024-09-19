from django.contrib import admin
from .models import Job,Category,Apply,Comment
from django.utils.translation import gettext_lazy as _
# Register your models here.
class MyJobAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('English'), {
            'fields': ('tags','title_en', 'location_en',  'description_en'),
        }),
        (_('Arabic'), {
            'fields': ('title_ar', 'location_ar',  'description_ar'),
        }),
        (_('Other'), {
            'fields': ('owner', 'vacancy', 'salary', 'experience','job_type', 'category', 'image', 'available', 'slug'),
        }),
    )
    readonly_fields = ('published_at',)

admin.site.register(Job, MyJobAdmin)
admin.site.register(Category)
admin.site.register(Apply)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'job', 'created', 'active'] 
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']


