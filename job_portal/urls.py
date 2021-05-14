from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('staff/', admin.site.urls),
    path('', include('pages.urls')),
    path('jobs/', include('jobs.urls')),
    path('accounts/', include('accounts.urls')),
    path('applications/', include('applications.urls')),
    path('contacts/', include('contacts.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

