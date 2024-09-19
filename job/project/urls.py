
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.urls import include,re_path



urlpatterns = i18n_patterns(
    path('i18n/',include('django.conf.urls.i18n')),
    path('setlang/', set_language, name='set_language'),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('account.urls', namespace='account')),
    path('',include('home.urls')),
    path('contact/',include('contact.urls',namespace='contact')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # path('',include('blog.urls')),
    path('myjob/',include('myjob.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),   
    path('blog/', include('blog.urls', namespace='blog')),
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

