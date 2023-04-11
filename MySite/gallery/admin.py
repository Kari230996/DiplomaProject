from django import forms
from django.contrib import admin
from .models import Gallery
from django.utils.safestring import mark_safe


# Register your models here.





class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    #fields = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'get_photo')
    
  
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "-"
        

    get_photo.short_description = 'Photo'

admin.site.register(Gallery, GalleryAdmin)

admin.site.site_title = 'Gallery settings'
admin.site.site_header = 'Gallery settings'

