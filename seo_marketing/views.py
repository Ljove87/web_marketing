from django.shortcuts import render
from . models import Post

def index_view(request):
    
    return render(request, 'seo_marketing/index_view.html')

def blog_view(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'seo_marketing/blog_view.html', context)

