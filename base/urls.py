
from django.urls import path
from .views import index, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)