from django.conf import settings
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Word2Domain apps Administration'
admin.site.site_title = 'Word2Domain apps Administration'
admin.site.index_title = "Portal administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('words/', include('w2d.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns


