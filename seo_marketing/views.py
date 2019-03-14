from django.shortcuts import render, redirect

from django.contrib import messages
from . models import Post
from django.core.mail import send_mail
from . forms import ContactForm

def index_view(request):
    return render(request, 'seo_marketing/index_view.html')

def blog_view(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'seo_marketing/blog_view.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            messages.success(request, f'Uspesno ste poslali poruku')
            return redirect('/')
            
    else:
        form = ContactForm()

    return render(request, 'seo_marketing/contact_view.html', {'form': form })

def about_view(request):
    return render(request, 'seo_marketing/about_view.html' )

