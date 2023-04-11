from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.conf import settings


from .models import Gallery
from .forms import ContactForm




class HomeGallery(ListView):
    model = Gallery
    template_name = 'gallery/home_gallery_list.html'
    context_object_name = 'gallery'
    #extra_content = {'title': 'Home'}
    #queryset = Gallery.objects.select_related('is_published')
    


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Homepage'
        
        return context
    
    def get_queryset(self):
        return Gallery.objects.filter(is_published=True)



class Show_gallery(ListView):
    model = Gallery
    template_name = 'gallery/show_gallery.html'
    context_object_name = 'gallery'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gallery'
        return context
    
    def get_queryset(self):
        return Gallery.objects.filter(is_published=True)

#class Contacts(CreateView):
#    form_class = ContactForm
#    template_name = 'gallery/contacts.html'
#    success_url = reverse_lazy('home')


# Create your views here.
#def index(request):
#    gallery = Gallery.objects.order_by('-created_at')
#    context = {
#        'gallery': gallery,
#          'title': 'Homepage'
#          }
#    return render(request, 'gallery/index.html', context)


#def show_gallery(request):
#    return render(request, 'gallery/show_gallery.html')


def about_us(request):
    return render(request, 'gallery/about_us.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # print(f"Name: {name}")
            # print(f"Email: {email}")
            # print(f"Subject: {subject}")
            # print(f"Message: {message}")
            try:
                # Create a new email message
                msg = EmailMessage(
                    subject=subject,
                    body=f"Name: {name}\nEmail: {email}\nMessage:\n {message}",
                    from_email=email,
                    to=[settings.MY_EMAIL_ADDRESS],
                    reply_to=[email],
                )
                # Send the email
                msg.send()

                messages.success(request, 'Your message has been sent', extra_tags='alert-success')
                return redirect('contacts')
            except Exception as e:
                messages.error(request, f'An error occurred while sending the email: {str(e)}', extra_tags='danger')
                print(f"Error: {e}")
        else:
            messages.error(request, 'Invalid form data', extra_tags='danger')
    else:
        form = ContactForm()
    return render(request, 'gallery/contacts.html', {'form': form})




