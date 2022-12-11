from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from accounts.views.example_view import ExampleView

urlpatterns = [
    path('', ExampleView.as_view(), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)