from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index-page'),
    path('blog/', views.blog_view, name='blog-page'),
    path('about/', views.about_view, name='about-page'),
    path('contact/', views.contact_view, name='contact-page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

