from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Painting'
        verbose_name_plural = 'Paintings'