from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('usluge/ketering/', views.ketering_view, name='ketering-page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

