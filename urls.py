from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('esteem'), permanent=True)),
    path('accounts/profile/', RedirectView.as_view(url=reverse_lazy('home'), permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('esteem/', include('esteem.urls')),
    path('home/', include('home.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

