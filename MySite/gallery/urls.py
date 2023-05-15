from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('', HomeGallery.as_view(), name='home'),
    path('gallery/show_gallery/', show_gallery, name='show_gallery'),
    path('gallery/about_us/', about_us, name='about-us'),
    path('gallery/contacts/', contacts, name='contacts'),




]