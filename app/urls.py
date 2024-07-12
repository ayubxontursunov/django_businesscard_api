from django.urls import path
from .views import root,RegisterAPIView,get_items
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", root),
    # path("register/",,name = 'register'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('card/<str:name>/', get_items, name='card'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
