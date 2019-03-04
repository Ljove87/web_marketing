from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index-page'),
    path('blog/', views.blog_view, name='blog-page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

