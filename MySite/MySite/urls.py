from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('i18n/', include('django.conf.urls.i18n')),

    path('', include('gallery.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += [
        path(
            "ckeditor5/",
            include('django_ckeditor_5.urls'),
            name="ck_editor_5_upload_file"
        ),
    ]

    urlpatterns += [
        path('captcha/', include('captcha.urls')),
    ]
