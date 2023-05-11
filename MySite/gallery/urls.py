from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    
    path('', HomeGallery.as_view(), name='home'),
    path('gallery/show_gallery/', Show_gallery.as_view(), name='show_gallery'), 
    path('gallery/painting/<int:pk>/', painting_detail, name='painting_detail'),
    path('gallery/about_us/', about_us, name='about-us'),
    path('gallery/contacts/', contacts, name='contacts'),

    #path('', index, name='home'),
    #path('', cache_page(60) (HomeGallery.as_view()), name='home'),
    #path('gallery/painting/<int:pk>/', PaintingDetailView.as_view(), name='painting_detail'),
    #path('gallery/contacts/', Contacts.as_view(), name='contacts'),


]