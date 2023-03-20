from django.shortcuts import render
from django.http import HttpResponse

from .models import Gallery

# Create your views here.
def index(request):
    gallery = Gallery.objects.order_by('-created_at')
    context = {
        'gallery': gallery,
          'title': 'Homepage'
          }
    return render(request, 'gallery/index.html', context)





