from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Gallery
from .forms import ContactForm

# Create your views here.
def index(request):
    gallery = Gallery.objects.order_by('-created_at')
    context = {
        'gallery': gallery,
          'title': 'Homepage'
          }
    return render(request, 'gallery/index.html', context)


def show_gallery(request):
    return render(request, 'gallery/show_gallery.html')


def about_us(request):
    return render(request, 'gallery/about_us.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        '''
        if form.is_valid():
            #print(form.cleaned_data)
            Gallery.objects.create(**form.cleaned_data)
            return redirect('home')
        '''
    else:
        form = ContactForm()
    
    return render(request, 'gallery/contacts.html', {'form': form})





