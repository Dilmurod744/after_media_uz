from django.conf.urls.static import static
from django.urls import path

from apps.views import UserTemplateView
from root import settings

urlpatterns = [
    path('', UserTemplateView.as_view(), name='main'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                        document_root=settings.MEDIA_ROOT)
