from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Gallery, GalleryImage


class PostAdminForm(forms.ModelForm):

    content = forms.CharField(
        widget=CKEditor5Widget(config_name='extends'),
        required=False
    )

    content_ru = forms.CharField(
        widget=CKEditor5Widget(config_name='extends'),
        required=False
    )

    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryImageInline(admin.TabularInline):

    model = GalleryImage

    extra = 1

    readonly_fields = (
        'get_image_preview',
    )

    fields = (
        'image',
        'get_image_preview',
    )

    def get_image_preview(self, obj):

        if obj.image:

            return mark_safe(
                f'<img src="{obj.image.url}" width="120" style="border-radius:10px;">'
            )

        return "-"

    get_image_preview.short_description = 'Preview'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    form = PostAdminForm

    save_as = True

    prepopulated_fields = {
        "slug": ("title",)
    }

    # =========================
    # LIST PAGE
    # =========================

    list_display = (
        'id',
        'title',
        'title_ru',
        'status',
        'price_rub',
        'price_eur',
        'price_usd',
        'is_published',
    )

    list_display_links = (
        'id',
        'title',
    )

    search_fields = (
        'title',
        'title_ru',
        'content',
        'content_ru',
        'materials',
    )

    list_editable = (
        'is_published',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'get_photo',
    )

    # =========================
    # FORM SECTIONS
    # =========================

    fieldsets = (

        ('English Content', {
            'fields': (
                'title',
                'content',
                'inspiration',
            )
        }),

        ('Russian Content', {
            'fields': (
                'title_ru',
                'content_ru',
                'inspiration_ru',
            )
        }),

        ('Main Image', {
            'fields': (
                'photo',
                'get_photo',
            )
        }),

        ('Painting Details', {
            'fields': (
                'slug',
                'width',
                'height',
                'materials',
                'year_created',
                'price_rub',
                'price_eur',
                'price_usd',
                'status',
            )
        }),

        ('Display Settings', {
            'fields': (
                'is_featured',
                'is_published',
            )
        }),

        ('Dates', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )

    inlines = [GalleryImageInline]

    # =========================
    # PREVIEW
    # =========================

    def get_photo(self, obj):

        if obj.photo:

            return mark_safe(
                f'<img src="{obj.photo.url}" width="180" style="border-radius:14px;">'
            )

        return "-"

    get_photo.short_description = 'Main Photo'


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'gallery',
        'get_image',
        'created_at',
    )

    search_fields = (
        'gallery__title',
        'gallery__title_ru',
    )

    readonly_fields = (
        'get_image',
    )

    def get_image(self, obj):

        if obj.image:

            return mark_safe(
                f'<img src="{obj.image.url}" width="120" style="border-radius:10px;">'
            )

        return "-"

    get_image.short_description = 'Preview'


admin.site.site_title = 'Gallery settings'
admin.site.site_header = 'Gallery settings'
