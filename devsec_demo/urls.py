"""
URL configuration for devsec_demo project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

# Custom 403 handler — renders a styled page instead of Django's plain default
handler403 = 'mupenz_fulgence.views.permission_denied_view'

urlpatterns = [
    path('', RedirectView.as_view(url='/auth/login/', permanent=False)),
    path('admin/', admin.site.urls),
    path('auth/', include('mupenz_fulgence.urls')),
]

# ── Development media serving ─────────────────────────────────────────────
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


