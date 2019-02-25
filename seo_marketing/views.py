from django.shortcuts import render

def index_view(request):
    return render(request, 'seo_marketing/index_view.html', {})
