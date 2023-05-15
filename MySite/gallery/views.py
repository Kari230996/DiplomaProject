from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView


from .models import Gallery
from .forms import ContactForm


class HomeGallery(ListView):
    model = Gallery
    template_name = 'gallery/home_gallery_list.html'
    context_object_name = 'gallery'
    #extra_content = {'title': 'Home'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Homepage'
        return context
    
    def get_queryset(self):
        return Gallery.objects.filter(is_published=True)







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





