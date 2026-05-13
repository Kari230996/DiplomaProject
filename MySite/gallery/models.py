from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField('Title', max_length=200)

    text = CKEditor5Field(
        'Text',
        config_name='extends'
    )


class Gallery(models.Model):

    STATUS_CHOICES = (
        ('available', _('Available')),
        ('sold', _('Sold')),
        ('private', _('Private Collection')),
    )

    # =========================
    # ENGLISH CONTENT
    # =========================

    title = models.CharField(
        max_length=150,
        verbose_name='Title'
    )

    content = CKEditor5Field(
        'Description',
        config_name='extends',
        blank=True
    )

    inspiration = models.TextField(
        blank=True,
        help_text='Short emotional story or inspiration',
        verbose_name='Inspiration'
    )

    # =========================
    # RUSSIAN CONTENT
    # =========================

    title_ru = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Название (RU)'
    )

    content_ru = CKEditor5Field(
        'Описание (RU)',
        config_name='extends',
        blank=True
    )

    inspiration_ru = models.TextField(
        blank=True,
        verbose_name='Вдохновение (RU)',
        help_text='Русская версия вдохновения'
    )

    # =========================
    # COMMON
    # =========================

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True
    )

    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True
    )

    width = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text='Width in cm'
    )

    height = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text='Height in cm'
    )

    materials = models.CharField(
        max_length=255,
        blank=True,
        help_text='Example: Oil on canvas'
    )

    year_created = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    price_rub = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    price_eur = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    price_usd = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    is_featured = models.BooleanField(
        default=False,
        help_text='Show on homepage'
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.title)

            slug = base_slug

            counter = 1

            while Gallery.objects.filter(slug=slug).exclude(pk=self.pk).exists():

                slug = f"{base_slug}-{counter}"

                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):

        return reverse(
            'home_gallery_list',
            kwargs={'pk': self.pk}
        )

    def __str__(self):

        return self.title

    class Meta:
        verbose_name = 'Painting'
        verbose_name_plural = 'Paintings'
        ordering = ['-created_at']


class GalleryImage(models.Model):

    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='gallery_extra/%Y/%m/%d/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Image for {self.gallery.title}"
