from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=CKEditor5Field('Text', config_name='extends')

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    

    def get_absolute_url(self):
        return reverse('home_gallery_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Painting'
        verbose_name_plural = 'Paintings'
        ordering = ['-created_at']