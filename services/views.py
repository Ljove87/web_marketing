from django.shortcuts import render

def ketering_view(request):
    return render(request, 'services/ketering.html')